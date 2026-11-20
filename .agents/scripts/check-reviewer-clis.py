#!/usr/bin/env python3
"""Check CLI installation, authentication evidence, and live model access."""

import argparse
import datetime
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import tempfile
import uuid


def run_command(command, cwd, timeout):
    process = subprocess.Popen(
        command, cwd=cwd, stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, start_new_session=True,
    )
    try:
        stdout, stderr = process.communicate(timeout=timeout)
        return process.returncode, stdout, stderr
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        stdout, stderr = process.communicate()
        return 124, stdout, stderr


def failure_reason(code, output):
    if code == 124:
        return "timeout"
    if code == 0:
        return "unexpected-response"
    text = output.lower()
    categories = (
        ("execution-permissions", ("operation not permitted", "permission denied")),
        ("authentication-required", ("not logged in", "not authenticated", "please log in",
                                     "please login", "invalid api key", "authentication required")),
        ("quota-or-rate-limit", ("quota", "rate limit", "usage limit", "insufficient credit")),
        ("model-unavailable", ("model not found", "unknown model", "model is not supported",
                               "do not have access to model")),
        ("network-error", ("connection refused", "could not resolve", "network is unreachable",
                           "failed to connect", "error sending request")),
        ("incompatible-cli", ("unknown flag", "unexpected argument", "unknown option")),
        ("configuration-error", ("invalid mcp configuration", "invalid configuration")),
    )
    for category, phrases in categories:
        if any(phrase in text for phrase in phrases):
            return category
    return "request-failed"


def check_cli(cli, args, cwd):
    model = {"codex": args.codex_model, "claude": args.claude_model,
             "agy": args.agy_model}[cli]
    result = {
        "cli": cli, "installed": bool(shutil.which(cli)), "version": None,
        "authentication": "unverified", "probe": "not-run", "model": model,
        "ready": False, "checked": datetime.datetime.now(
            datetime.timezone.utc).isoformat(),
    }
    if not result["installed"]:
        result["next_action"] = f"Install {cli} and rerun the check."
        return result

    code, stdout, _ = run_command([cli, "--version"], cwd, 10)
    version = re.search(r"\d+\.\d+\.\d+[^\s]*", stdout)
    if code != 0 or not version:
        result["probe"] = "cli-error"
        result["next_action"] = f"Check {cli} --version and the installed CLI."
        return result
    result["version"] = version.group()
    if args.presence_only:
        result["next_action"] = "Rerun without --presence-only to verify readiness."
        return result

    if cli == "codex":
        code, stdout, stderr = run_command([cli, "login", "status"], cwd, 10)
        if code == 0 and "logged in" in (stdout + stderr).lower():
            result["authentication"] = "configured"
    elif cli == "claude":
        code, stdout, _ = run_command([cli, "auth", "status", "--json"], cwd, 10)
        try:
            auth = json.loads(stdout)
            if auth.get("loggedIn") is True:
                result["authentication"] = "configured"
            elif auth.get("loggedIn") is False:
                result["authentication"] = "not-authenticated"
        except (ValueError, AttributeError):
            pass

    token = "CLI_READY_" + uuid.uuid4().hex
    prompt = (
        f"This is a connectivity check. Reply with exactly {token} and nothing "
        "else. Use no tools, read no files, and make no changes."
    )
    last_message = Path(cwd) / "codex-response.txt"
    commands = {
        "codex": [
            cli, "exec", "--sandbox", "read-only", "--skip-git-repo-check",
            "--ephemeral", "--output-last-message", str(last_message),
            "--model", model, prompt,
        ],
        "claude": [
            cli, "-p", prompt, "--model", model, "--tools", "",
            "--strict-mcp-config", "--mcp-config", '{"mcpServers": {}}',
            "--disable-slash-commands", "--no-session-persistence",
            "--output-format", "text",
        ],
        "agy": [
            cli, "--mode", "plan", "--model", model,
            "--print-timeout", f"{args.timeout}s", "-p", prompt,
        ],
    }
    code, stdout, stderr = run_command(commands[cli], cwd, args.timeout)
    response = stdout.strip()
    if cli == "codex" and last_message.is_file():
        response = last_message.read_text().strip()
    result["probe_exit_code"] = code
    if code == 0 and response == token:
        result.update(authentication="verified-by-request", probe="passed", ready=True)
    else:
        result["probe"] = "timeout" if code == 124 else "failed"
        result["failure"] = failure_reason(code, stdout + stderr)
        result["next_action"] = (
            f"Check {cli} login, access to {model}, quota, network and CLI flags. "
            "Rerun this CLI check after resolving the failure."
        )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", choices=["codex", "claude", "agy"], action="append")
    parser.add_argument("--presence-only", action="store_true",
                        help="Check installation only, without model requests.")
    parser.add_argument("--timeout", type=int, default=60,
                        help="Maximum seconds for each live request.")
    parser.add_argument("--codex-model", default="gpt-6.1-sol")
    parser.add_argument("--claude-model", default="sonnet")
    parser.add_argument("--agy-model", default="gemini-4-neon-high")
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")

    results = []
    for cli in dict.fromkeys(args.cli or ["codex", "claude", "agy"]):
        with tempfile.TemporaryDirectory(prefix="cc-cli-check-") as cwd:
            try:
                result = check_cli(cli, args, cwd)
            except OSError:
                result = {
                    "cli": cli, "ready": False, "probe": "environment-error",
                    "authentication": "unverified",
                    "next_action": "Check process permissions and rerun this CLI check.",
                }
            results.append(result)
            print(json.dumps(result), flush=True)
    return 0 if args.presence_only or all(item["ready"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

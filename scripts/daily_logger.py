#!/usr/bin/env python3
"""
============================================================
Way to Python - Daily Progress Logger & GitHub Auto-Sync
============================================================
This script automates:
1. Updating the README.md Progress Table & Stats
2. Staging day-wise code files
3. Creating conventional git commit messages
4. Pushing commits directly to GitHub
============================================================
"""

import os
import sys
import re
import subprocess
import argparse
from datetime import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
README_PATH = os.path.join(REPO_ROOT, "README.md")


def run_command(cmd, check=True):
    """Executes a shell command inside the repo root."""
    print(f"👉 Running: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=REPO_ROOT, capture_output=True, text=True)
    if check and res.returncode != 0:
        print(f"❌ Error (exit code {res.returncode}):\n{res.stderr.strip()}")
        return None
    return res.stdout.strip()


def get_git_status():
    """Returns clean/dirty status."""
    return run_command("git status --porcelain", check=False)


def update_readme(day: int, topic: str, file_name: str, concepts: str, date_str: str):
    """Updates the Daily Progress Tracker in README.md."""
    if not os.path.exists(README_PATH):
        print(f"⚠️ README.md not found at {README_PATH}")
        return False

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Form table row
    file_link = f"[{file_name}](./{file_name.replace(' ', '%20')})" if file_name else "N/A"
    new_row = f"| **Day {day:02d}** | {date_str} | **{topic}** | `{concepts}` | {file_link} | ✅ Completed |"

    # Check if this day is already recorded in the table
    day_pattern = rf"\|\s*\*\*Day {day:02d}\*\*.*\|"
    if re.search(day_pattern, content):
        print(f"ℹ️ Day {day:02d} entry already found in README. Updating line...")
        content = re.sub(day_pattern, new_row, content)
    else:
        # Search for table marker
        marker = "<!-- DAILY_TRACKER_ROWS -->"
        if marker in content:
            content = content.replace(marker, f"{new_row}\n{marker}")
        else:
            # Fallback search for table header
            table_header_end = "| :--- | :--- | :--- | :--- | :--- | :--- |"
            if table_header_end in content:
                content = content.replace(table_header_end, f"{table_header_end}\n{new_row}")
            else:
                print("⚠️ Could not locate table insert point in README.md.")
                return False

    # Update Days Logged counter badge if present
    # Example pattern: ![Days Completed](https://img.shields.io/badge/Days%20Completed-X-brightgreen)
    def badge_repl(match):
        badge_prefix = match.group(1)
        return f"{badge_prefix}{day}-brightgreen"

    content = re.sub(r"(!\[Days Completed\]\(https://img\.shields\.io/badge/Days%20Completed-)\d+(-brightgreen)",
                     badge_repl, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ README.md updated successfully for Day {day:02d}!")
    return True


def git_commit_and_push(day: int, topic: str, push: bool = True):
    """Stages changes, commits with conventional commit message, and pushes."""
    print("\n📦 Staging changes...")
    run_command("git add .")

    commit_msg = f"feat(day-{day:02d}): {topic.lower()} practice & notes"
    print(f"📝 Committing: '{commit_msg}'")
    run_command(f'git commit -m "{commit_msg}"')

    if push:
        print("\n🚀 Pushing to GitHub (origin main)...")
        push_res = run_command("git push -u origin main", check=False)
        if push_res is not None:
            print("🎉 Successfully pushed to GitHub!")
        else:
            print("⚠️ Push failed or remote not reachable yet. You can push manually using `git push -u origin main`.")


def main():
    parser = argparse.ArgumentParser(description="Log daily Python progress to README and commit to GitHub.")
    parser.add_argument("--day", type=int, help="Day number (e.g., 1)")
    parser.add_argument("--topic", type=str, help="Topic name (e.g., 'Bitwise Operators')")
    parser.add_argument("--file", type=str, help="Code filename (e.g., 'D1 Bitwise.py')")
    parser.add_argument("--concepts", type=str, help="Brief key concepts (e.g., 'AND, OR, XOR, Shifts, Bitmasks')")
    parser.add_argument("--no-push", action="store_true", help="Commit only without pushing")
    
    args = parser.parse_args()

    # If arguments not provided, ask interactively
    if not (args.day and args.topic):
        print("=" * 60)
        print("  🐍 Way to Python - Daily Learning Logger")
        print("=" * 60)
        try:
            day_in = input("Enter Day Number (e.g., 1): ").strip()
            day = int(day_in)
            topic = input("Enter Topic Name (e.g., Bitwise Operators): ").strip()
            file_name = input("Enter Python file name (e.g., D1 Bitwise.py): ").strip()
            concepts = input("Enter Key Concepts learned: ").strip()
            push_in = input("Push to GitHub immediately? (y/n, default: y): ").strip().lower()
            push = push_in != "n"
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            sys.exit(0)
    else:
        day = args.day
        topic = args.topic
        file_name = args.file or ""
        concepts = args.concepts or topic
        push = not args.no_push

    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # 1. Update README
    update_readme(day, topic, file_name, concepts, date_str)

    # 2. Git Commit and Push
    git_commit_and_push(day, topic, push=push)


if __name__ == "__main__":
    main()

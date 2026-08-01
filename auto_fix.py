import os
import subprocess
from git import Repo
from github import Github

REPO_NAME = "cloudaws305/test"
BRANCH = "ai-auto-fix_1"
FILE = "app.py"

# Read file
with open(FILE, "r") as f:
    code = f.read()

# Very simple "AI" fix
if "1/0" in code:
    print("Found division by zero. Fixing...")

    code = code.replace("1/0", "1")

    with open(FILE, "w") as f:
        f.write(code)

else:
    print("No known issue found.")
    exit(1)

# Verify fix
result = subprocess.run(["python3", FILE])

if result.returncode != 0:
    print("Fix verification failed.")
    exit(1)

print("Verification passed.")

# Git operations

token = "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"

github = Github(token)

username = "cloudaws305"
repo = Repo(".")
repo.remote().set_url(
    f"https://{username}:{token}@github.com/cloudaws305/test.git"
)
try:
    repo.git.checkout("-b", BRANCH)
except Exception:
    repo.git.checkout(BRANCH)

repo.git.add(FILE)

if repo.is_dirty():
    repo.index.commit("Auto fix: Division by zero")
    repo.remote().push(BRANCH)
else:
    print("No changes to commit.")
    exit(0)



repo_obj = github.get_repo(REPO_NAME)

repo_obj.create_pull(
    title="Auto Fix: Division by zero",
    body="Automatically fixed by Jenkins.",
    head=BRANCH,
    base="main"
)

print("Pull Request created successfully.")

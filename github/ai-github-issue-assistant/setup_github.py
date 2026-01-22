#!/usr/bin/env python3
"""
GitHub Setup Script - Push local repository to GitHub
Run this after installing Git from https://git-scm.com/download/win
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and report status"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {description} - SUCCESS")
            return True
        else:
            print(f"✗ {description} - FAILED")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ {description} - ERROR: {e}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("GitHub Repository Setup")
    print("=" * 60)
    
    # Get repository info
    print("\nPlease provide the following information:")
    github_user = input("Your GitHub username: ").strip()
    repo_name = "ai-github-issue-assistant"
    
    if not github_user:
        print("Error: GitHub username is required")
        sys.exit(1)
    
    remote_url = f"https://github.com/{github_user}/{repo_name}.git"
    
    print(f"\nRepository URL: {remote_url}")
    print("\nMake sure you have:")
    print("1. Created the repository on GitHub (https://github.com/new)")
    print("2. Installed Git (https://git-scm.com/download/win)")
    print("3. Configured Git credentials (git config --global user.name/email)")
    
    confirm = input("\nReady to proceed? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Setup cancelled")
        sys.exit(0)
    
    print("\n" + "=" * 60)
    print("Executing Git commands...")
    print("=" * 60)
    
    # Commands to execute
    commands = [
        (f'git remote add origin {remote_url}', "Add remote origin"),
        ("git branch -M main", "Rename branch to main"),
        ("git push -u origin main", "Push to GitHub"),
    ]
    
    success = True
    for cmd, description in commands:
        if not run_command(cmd, description):
            success = False
            break
    
    print("\n" + "=" * 60)
    if success:
        print("✓ Setup completed successfully!")
        print(f"Your repository is available at: {remote_url}")
    else:
        print("✗ Setup encountered errors")
        print("Please troubleshoot and try again")
    print("=" * 60)

if __name__ == "__main__":
    main()

import requests
from typing import Optional, Dict, List
import os


class GitHubHandler:
    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"

    def parse_repo_url(self, url: str) -> tuple:
        """Extract owner and repo from GitHub URL"""
        url = url.strip().rstrip("/")
        parts = url.replace("https://github.com/", "").replace("http://github.com/", "").split("/")
        if len(parts) < 2:
            raise ValueError("Invalid GitHub URL format. Use: https://github.com/owner/repo")
        return parts[0], parts[1]

    def get_issue(self, owner: str, repo: str, issue_number: int) -> Dict:
        """Fetch issue details from GitHub"""
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_issue_comments(self, owner: str, repo: str, issue_number: int) -> List[Dict]:
        """Fetch all comments for an issue"""
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}/comments"
        all_comments = []
        page = 1
        
        while True:
            params = {"page": page, "per_page": 100}
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            comments = response.json()
            
            if not comments:
                break
            
            all_comments.extend(comments)
            page += 1
        
        return all_comments

    def fetch_complete_issue(self, repo_url: str, issue_number: int) -> Dict:
        """Fetch complete issue with all comments"""
        try:
            owner, repo = self.parse_repo_url(repo_url)
            
            issue = self.get_issue(owner, repo, issue_number)
            comments = self.get_issue_comments(owner, repo, issue_number)
            
            return {
                "title": issue.get("title", ""),
                "body": issue.get("body", ""),
                "comments": [{"body": c.get("body", ""), "user": c.get("user", {}).get("login", "")} for c in comments],
                "labels": [label.get("name", "") for label in issue.get("labels", [])],
                "state": issue.get("state", ""),
                "created_at": issue.get("created_at", ""),
                "updated_at": issue.get("updated_at", ""),
            }
        except Exception as e:
            raise Exception(f"Error fetching issue: {str(e)}")

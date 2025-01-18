#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to the oldest) of
a repository by a given owner using the GitHub API.
"""

if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

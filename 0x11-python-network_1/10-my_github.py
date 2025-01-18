#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token),
uses the GitHub API to display the user's id.
"""
if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")

#!/usr/bin/python3
"""
This script takes in a URL and an Email, sends
a POST request to the passed URL with the email
as a parameter, and displays the body of the
response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    # Retrieve the URL and email from the cmd-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create the POST data as a dictionary and encode it
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Send the POST request
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode("utf-8")
        print(body)

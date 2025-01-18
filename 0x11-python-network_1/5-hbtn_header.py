#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the vlue of the variable X-Request-Id in
the response header.
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)

#!/usr/bin/python3
"""
this script takes a URL, sends a request to the URL,
and displays the value of the X-Request-id variable found
in the header of the response.
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        # Fetch the header value of X-Request-Id into x_request_id
        x_request_id = response.headers.get("X-Request-Id")
        print(x_request_id)

#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
If an HTTP error occurs, it prints error code.
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    # Retrieve the url from the command-line arguments
    url = sys.argv[1]

    try:
        # Send the request to the URL
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors by printing the error code
        print("Error code: {}".format(e.code))

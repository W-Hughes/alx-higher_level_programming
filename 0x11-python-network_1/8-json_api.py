#!/usr/bin/python3
"""
This cript takes in a letter and sends a POST request to a URL
http://0.0.0.0:5000/search_user with the letter as a parameter
stored in q.
If no argument is given q is set to an empty string.
If the response body is property JSON formatted and not empty,
name and id are dsplayed as [<id>] <name>
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

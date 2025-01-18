#!/usr/bin/python3
"""
this script fetches the URL https://alx-intranet.hbtn.io/status
and display the body in a required format.
"""
if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    with requests.get(url):
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))

#!/bin/bash
# Sends a GET request to the URl passed as an argument and displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"

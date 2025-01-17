#!/bin/bash
# Sends a DELETE request to the URL passes as the first argument and diplays the body of the response
curl -sX DELETE "$1"

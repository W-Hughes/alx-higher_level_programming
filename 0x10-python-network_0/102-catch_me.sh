#!/bin/bash
# Makes a request to a catch_me URL that causes the server to respond with a message "You got me!"
curl -sL -X GET -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me

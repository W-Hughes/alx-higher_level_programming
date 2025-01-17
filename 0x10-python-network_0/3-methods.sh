#!/bin/bash
# Dsplays all HTTP methos the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-

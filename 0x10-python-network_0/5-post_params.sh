#!/bin/bash
# Sends a POST request with specific parameters and displays the respose body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

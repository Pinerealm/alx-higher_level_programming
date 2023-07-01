#!/bin/bash
# Send a POST request with variables, and display the response body
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

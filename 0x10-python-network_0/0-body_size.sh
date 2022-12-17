#!/bin/bash
# This script displays the size of the body of the response froma server
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2

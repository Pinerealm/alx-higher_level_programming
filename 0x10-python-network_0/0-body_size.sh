#!/bin/bash
# This script displays the size of the response body from a server
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2

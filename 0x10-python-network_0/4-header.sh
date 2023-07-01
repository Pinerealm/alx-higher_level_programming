#!/bin/bash
# Send a request with a custom header variable, and display the response body
curl -sH "X-School-User-Id: 98" "$1"

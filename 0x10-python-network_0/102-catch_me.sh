#!/bin/bash
# Make a request that causes the server to respond with 'You got me!'
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me

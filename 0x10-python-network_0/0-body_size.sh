#!/usr/bin/env bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Get the URL from the user
url=$1

# Send a request to the URL
response=$(curl -Is $url)

# Get the size of the response body
body_size=$(echo $response | grep -Eo 'Content-Length: [0-9]+' | cut -d ':' -f 2)

# Display the size of the response body
echo $body_size


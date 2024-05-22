#!/bin/bash
#curl body size

if [ $# -lt 1 ]; then
	echo "usage: $0 <URL>"
	exit 1
fi
response=$(curl -sI "$1")
content_length=$(echo "$response" | grep -oP '(?<=Content-Length: ).*')
echo "$content_length"

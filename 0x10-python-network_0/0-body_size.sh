#!/bin/bash
#curl body size
echo $(curl -sI "$1" | grep -oP '(?<=Content-Length: ).*')

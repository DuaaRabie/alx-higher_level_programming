#!/bin/bash
#curl to the end
curl -s -X DELETE -o /dev/null -w "" "$1" && curl -s -L "$1"

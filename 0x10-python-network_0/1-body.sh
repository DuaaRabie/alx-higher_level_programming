#!/bin/bash
#curl to the end
curl -s -L -o /dev/null -w "" "$1" && curl -s -L "$1"

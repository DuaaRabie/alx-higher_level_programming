#!/bin/bash
#curl to the end
curl -s -o /dev/null -w "" "$1" && curl -s "$1"

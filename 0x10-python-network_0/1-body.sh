#!/bin/bash
#curl to the end
curl -s -o /dev/null -w "%{http_code}" "$1" && curl -s "$1"

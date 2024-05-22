#!/bin/bash
#curl to the end
echo $(curl -s -o /dev/null -w "%{http_code}" "$1" && curl -s "$1")

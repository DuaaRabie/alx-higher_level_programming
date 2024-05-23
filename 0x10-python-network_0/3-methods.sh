#!/bin/bash
#curl only methods
curl -s -I "$1" | awk '/^Allow: /' | sed '/^Allow: / s/^Allow: //'

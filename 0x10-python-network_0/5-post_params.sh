#!/bin/bash
#curl Post parameters
curl -s -H "Content-Type: application/json" -H "email: test@gmail.com" -H "subject: I will always be here for PLD" -X POST "$1"

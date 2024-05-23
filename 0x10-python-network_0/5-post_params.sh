#!/bin/bash
#curl Post parameters
curl -s -H "Content-Type: application/json" -d '"email": "test@gmail.com", "subject": "I will always be here for PLD"}' -X POST "$1"

#!bin/bash
#count characters of output
curl -s "$1" | wc -c

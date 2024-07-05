#!/usr/bin/python3
import urllib.request
import json
import urllib.parse

url = 'https://httpbin.org/post'
values = {
    'key1': 'value1',
    'key2': 'value2'
}

# Convert the data to a JSON string
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
headers = {'Content-Type': 'application/json'}

# Create a request object
req = urllib.request.Request(url, data, headers)

# Make the request and read the response
with urllib.request.urlopen(req) as response:
    response_data = response.read().decode('utf-8')
    print(response_data)

#!/usr/bin/python3
'making a post request in python requests'
if __name__ == "__main__":
    import requests
    import json
    data = {"key":"value"}
    print(type(data))
    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json"} 
    url = 'https://httpbin.org/post'
    response = requests.post(url,data=json_data, headers=headers)
    print(response.json())

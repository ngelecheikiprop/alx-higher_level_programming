#!/usr/bin/python3
'getting data then checking it'
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {"q": q}
    response = requests.post(url, data)
    data = response.json()
    if not isinstance(data, dict):
        print("Not a valid JSON")
    if not data:
        print("No result")
    else:
        print("[{}] {}".format(data.get('id'), data.get('name')))

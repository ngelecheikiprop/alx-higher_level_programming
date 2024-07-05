#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    if  len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {"q":q}
    response = requests.post(url, data)
    print(type(response.json()))

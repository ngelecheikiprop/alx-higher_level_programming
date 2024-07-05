#!/usr/bin/python3
'getting header of a response using requests'
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])

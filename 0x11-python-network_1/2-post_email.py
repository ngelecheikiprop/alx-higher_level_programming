#!/usr/bin/python3
'post and email then print the response'
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email":email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

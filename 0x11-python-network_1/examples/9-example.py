#!/usr/bin/python3
'Testing url errors'
if __name__ == "__main__":
    import urllib.request
    url = 'https://httpbin.org/status/404'
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e)

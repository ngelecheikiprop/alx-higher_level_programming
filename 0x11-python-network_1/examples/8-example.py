#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    url = 'http://cannot/exist'
    req = urllib.request.Request(url)
    try :
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print("----------",e)

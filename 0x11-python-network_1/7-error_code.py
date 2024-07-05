#!/usr/bin/python3
'if errors print the ones over 400'
if __name__ == "__main__":
    import requests
    import sys
    url = sys[1]
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    elif response.status_code > 400:
        print("Error code:", response.status_code)

#!/usr/bin/python3
""" url using request fetching """


if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    with requests.get(url) as r:
        content = r.text
        print(f"Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")

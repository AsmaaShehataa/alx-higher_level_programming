#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
  import requests

  url = 'https://alx-intranet.hbtn.io/status'

  with requests.get(url) as r:
        content = r.text
        print(f"Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")

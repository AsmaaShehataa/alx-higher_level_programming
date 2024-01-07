#!/usr/bin/python3
'''Evaluation of Holberton technical back end'''

if __name__ == '__main__':
    import requests
    import sys

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    headers = {
              'Accept': 'application/vnd.github.v3+json',
              }
    params = {
        'per_page': 10,
    }

    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
                      owner_name, repository_name),
                      headers=headers, params=params)
    json_res = res.json()
    for commit in json_res:
        print(commit['sha'] + ':', commit['commit']['author']['name'])

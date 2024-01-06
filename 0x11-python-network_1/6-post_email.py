#!/usr/bin/python3
""" post email data into the url """

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]

    my_params = {'email': email}
    my_result = requests.post(url, my_params)
    print(my_result.text)

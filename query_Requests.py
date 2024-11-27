"""
    Request Implementation of Querying API

    Dependencies: Requests library

    Documentation: https://requests.readthedocs.io/en/latest/
"""

import requests

def query(token: str, query: str, sort: str, order: str,num_repo):
    url = 'https://api.github.com/search/repositories'

    params = {}
    if sort and order:
        params['q'] = query
        params['sort'] = sort
        params['order'] = order
        params['per_page'] = num_repo
        print(f"--------------------------------------\nQuery:{query}\nSorting By:{sort}\nOrdering:{order}\n--------------------------------------\n")

    elif sort:
        params['q'] = query
        params['sort'] = sort
        params['per_page'] = num_repo
        print(f"--------------------------------------\nQuery:{query}\nSorting By:{sort}\n--------------------------------------\n")

    elif order:
        params['q'] = query
        params['order'] = order
        params['per_page'] = num_repo
        print(f"--------------------------------------\nQuery:{query}\nOrdering:{order}\n--------------------------------------\n")

    else:
        params['q'] = query
        print(f"--------------------------------------\nQuery:{query}\n--------------------------------------\n")


    headers={
        'Authorization': f'token {token}'
    }

    response = requests.get(url, headers=headers,params=params)

    if response.status_code == 200:
        repos = response.json()

        total_count = repos['total_count']
        print(f"Total repos found:{total_count}\n")

        print(f"Top {num_repo} Repositories:")
        counter = 0
        for repo in repos['items']:
            counter += 1
            print(f"{counter}) Repository Name: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"URL: {repo['html_url']}\n")
        return repos
    else:
        print(f"Request Failed... Exiting")
        return 1

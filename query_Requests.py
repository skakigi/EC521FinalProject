"""
    Request Implementation of Querying API

    Dependencies: Requests library

    Documentation: https://requests.readthedocs.io/en/latest/
"""

import requests

def query(token: str, query: str, sort: str, order: str,num_repo):
    url = 'https://api.github.com/search/repositories'

    per_page = 50
    pages = num_repo//per_page + (1 if num_repo%per_page != 0 else 0)

    repos = []
    total_count = 0
    if sort and order:
        print(f"--------------------------------------\nQuery:{query}\nSorting By:{sort}\nOrdering:{order}\n--------------------------------------\n")
    elif sort:
        print(f"--------------------------------------\nQuery:{query}\nSorting By:{sort}\n--------------------------------------\n")
    elif order:
        print(f"--------------------------------------\nQuery:{query}\nOrdering:{order}\n--------------------------------------\n")
    else:
        print(f"--------------------------------------\nQuery:{query}\n--------------------------------------\n")

    for page in range(1,pages+1):
        params = {}
        if sort and order:
            params['q'] = query
            params['sort'] = sort
            params['order'] = order
            params['per_page'] = per_page
            params['page'] = page
        elif sort:
            params['q'] = query
            params['sort'] = sort
            params['per_page'] = per_page
            params['page'] = page
        elif order:
            params['q'] = query
            params['order'] = order
            params['per_page'] = per_page
            params['page'] = page
        else:
            params['q'] = query
            params['per_page'] = per_page
            params['page'] = page
        headers = {
            'Authorization': f'token {token}'
        }

        response = requests.get(url, headers=headers,params=params)

        if response.status_code == 200:
            repos.extend(response.json()['items'])
            if total_count == 0:
                total_count = response.json()['total_count']
        else:
            break

    if repos:
        print(f"Total repos found:{total_count}\n")

        print(f"Top {num_repo} Repositories:")
        counter = 0
        for repo in repos[:num_repo]:
            counter += 1
            print(f"{counter}) Repository Name: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"URL: {repo['html_url']}\n")
        return repos
    else:
        print(f"Request Failed... Exiting")
        return 1

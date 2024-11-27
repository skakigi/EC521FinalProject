"""
    PyGithub Implementation of Search Query

    Dependencies: PyGithub (NOT github!!!!)

    Takes your token, and various search parameters (if empty string is passed, ignores parameter)
"""

from github import Github

def query(token:str,query:str,sort:str,order:str,num_repo:int):

    g_token = Github(token)

    if sort and order:
        print(f"--------------------------------------\nQuery:{query}\nSorting By:{sort}\nOrdering:{order}\n--------------------------------------\n")
        repos = g_token.search_repositories(query=query, sort=sort, order=order)
    elif sort:
        print(f"--------------------------------------\nQuery:{query}\nSorting By:{sort}\n--------------------------------------\n")
        repos = g_token.search_repositories(query=query, sort=sort)
    elif order:
        print(f"--------------------------------------\nQuery:{query}\nOrdering:{order}\n--------------------------------------\n")
        repos = g_token.search_repositories(query=query, order=order)
    else:
        print(f"--------------------------------------\nQuery:{query}\n--------------------------------------\n")
        repos = g_token.search_repositories(query=query)


    total_count = repos.totalCount
    print(f"Total repos found:{total_count}\n")

    print(f"Top {num_repo} Repositories:")

    counter=0
    for repo in repos[:num_repo]:
        counter+=1
        print(f"{counter}) Repository Name: {repo.full_name}")
        print(f"Description: {repo.description}")
        print(f"Stars: {repo.stargazers_count}")
        print(f"URL: {repo.url}\n")

    return repos
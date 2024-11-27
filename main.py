import os
import sys
import get_tokens
import query_PyGithub
import query_Requests

# --------------------------------------- Parameters --------------------------------------- #

""" If using testing inputs: set to 1, If using User Input: set to 0"""
testing = 0

"""If using PyGithub Version: set to 1, if using Requests Version: set to 0"""
PyGithub = 0

# --------------------------------------- Start of Program --------------------------------------- #

# Retrieve Token from .env & Check
print("--------------------------------------\nGetting Github Token From Environment...\n")
token = get_tokens.retrieve_token()

if not token:
  sys.exit("Failed to retrieve Github Token... Check your .env file...\nExiting\n--------------------------------------")
else:
    print("Github Token Retrieved\nContinuing...\n--------------------------------------\n")



# --------------------------------------- Testing Input Version --------------------------------------- #

# Determine Search Parameters DO NOT DELETE VARS JUST SET TO ""
# Note: you NEED a query

if testing:
    """
    query examples: 
        topic:public-api  (looks for public api)
        API language:Python (looks for any api using python)    
    """
    query = "API language:Python"

    """
    sort examples: 
        stars (uses stargazers count)
    """
    sort = "stars"

    """
    order examples:
        desc (descending order)
        asc (ascending order)
    """

    order = "desc"

    num_repo=10

# --------------------------------------- End of Test Version --------------------------------------- #

# --------------------------------------- User Input Version --------------------------------------- #

else:

    print("Query examples:\n -topic:public-api  (looks for public api)\n -API language:Python (looks for any api using python)\n")
    query = input("Enter Query:")
    print("\n")

    print("Sort examples:\n -stars (uses stargazers count)\n")
    sort = input("Enter Sort:")
    print("\n")

    print("Order examples:\n -desc (descending order)\n -asc (ascending order)\n")
    order = input("Enter Order:")
    print("\n")

    num_repo_str = input("Enter How Many Repositories to Display:")
    num_repo = int(num_repo_str)
    print("\n")

# --------------------------------------- End of User Request Version --------------------------------------- #

# --------------------------------------- Query Function Choice --------------------------------------- #
"""
 Use either query_PyGithub or query_Requests 
    -still unsure if one is better than the other (im pretty sure PyGithub just calls requests)
"""


if PyGithub:
    print("Searching using PyGithub...\n")
    repos = query_PyGithub.query(token, query, sort,order,num_repo)
else:
    print("Searching using Requests...\n")
    repos = query_Requests.query(token, query, sort,order,num_repo)
    if repos == 1:
        sys.exit("Failed to retrieve requests")






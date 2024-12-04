import os
import sys
import authcheck_Requests
import get_tokens
import query_PyGithub
import query_Requests
import CSV
from tqdm import tqdm


"""
    Main execution file for API Scraping Tool
    
    Check Parameters section before running
    
    If testing is off (user input is on), type in your requested sections into terminal or leave empty if unwanted
"""
# --------------------------------------- Parameters --------------------------------------- #

""" If default inputs: set to True, If using User Input: set to False"""

in_default = input("Do you want to use default parameters? (y/n): ")
while in_default != "y" and in_default != "n" and in_default != "Y" and in_default != "N":
    in_default = input("Error: Enter a Valid Input\nDo you want to use default parameters? (y/n): ")
if in_default == "y" or in_default == "Y":
    default = True
    print("Using default parameters...\n")
else:
    default = False
    print("Using user input parameters...\n")

"""If using PyGithub Version: set to 1, if using Requests Version: set to 0"""
in_PyGithub = input("Do you want to use PyGithub Version? (y/n): ")
while in_PyGithub != "y" and in_PyGithub != "n" and in_PyGithub != "y" and in_PyGithub != "N" and in_PyGithub != "Y":
    in_PyGithub = input("Error: Enter a Valid Input\nDo you want to use PyGithub Version? (y/n): ")
if in_PyGithub == "y" or in_PyGithub == "Y":
    PyGithub = True
    print("Using PyGithub Version...\n")
else:
    PyGithub = False
    print("Using Requests Version...\n")


# --------------------------------------- Start of Program --------------------------------------- #

# Retrieve Token from .env & Check
print("--------------------------------------\nGetting Github Token From Environment...\n")
token = get_tokens.retrieve_token()

if not token:
  sys.exit("Failed to retrieve Github Token... Check your .env file...\nExiting\n--------------------------------------")
else:
    print("Github Token Retrieved\nContinuing...\n--------------------------------------\n")



# --------------------------------------- Testing Input Version --------------------------------------- #

# Determine Search Parameters
# Note: you NEED a query

""" !!! DO NOT DELETE VARIABLES JUST SET TO "" !!! """
if default:
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
    - PyGithub currently runs faster than Requests, unsure if its implementation or the PyGithub library is just better
"""

"""Clear all data from csv"""
CSV.clear_data()

"""Request Data"""
if PyGithub:
    print("Searching using PyGithub...\n")
    repos = query_PyGithub.query(token, query, sort,order,num_repo)
    total_count = repos.totalCount
    if total_count:
        for repo in tqdm(repos[:min(total_count,num_repo)], total=min(total_count,num_repo), desc="Writing to CSV", unit="repo"):
            auth_vuln = 0
            # TODO: make the auth_check better
            if authcheck_Requests.check_auth(repo.url):
                authVuln = 1
            CSV.write_data_PyGithub(repo, auth_vuln)
    else:
        sys.exit("No valid repositories found")
else:
    print("Searching using Requests...\n")
    repos = query_Requests.query(token, query, sort,order,num_repo)
    total_count = len(repos)
    if total_count == 0:
        sys.exit("Failed to retrieve requests")
    else:
        for repo in tqdm(repos[:min(num_repo,total_count)],total = min(num_repo,total_count), desc="Writing to CSV",unit="repo"):
            auth_vuln=0
            #TODO: make the auth_check better
            if authcheck_Requests.check_auth(repo['html_url']):
                authVuln=1
            CSV.write_data(repo,auth_vuln)

    print("All Done!\n\n")







import requests

#TODO: Make this better, this doesnt mean anything really just testing a request
def check_auth(api):
    response = requests.get(api)
    if response.status_code == 200:
        return 1
    else:
        return 0

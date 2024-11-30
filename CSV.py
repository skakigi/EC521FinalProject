import pandas as pd
import os

file_name = "Repo_Vulnerability.csv"

def write_data(repo,auth_vuln):
    data = {
        "Repo": [repo['html_url']],
        "Auth Secure?": "No" if auth_vuln else "Yes",
    }
    df = pd.DataFrame(data)

    if os.path.exists(file_name) and os.path.getsize(file_name)>0:
        df.to_csv(file_name,mode='a',index=False,header=False)
    else:
        df.to_csv(file_name,mode='w',index=False,header=True)

def write_data_PyGithub(repo,auth_vuln):
    data = {
        "Repo": [repo.url],
        "Auth Secure?": "No" if auth_vuln else "Yes",
    }
    df = pd.DataFrame(data)

    if os.path.exists(file_name) and os.path.getsize(file_name)>0:
        df.to_csv(file_name,mode='a',index=False,header=False)
    else:
        df.to_csv(file_name,mode='w',index=False,header=True)

def clear_data():
    if os.path.exists(file_name):
        with open(file_name,'w') as file:
            pass

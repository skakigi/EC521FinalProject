from dotenv import load_dotenv
import os
# --------------------------------------- Function Definitions --------------------------------------- #

def retrieve_token():

    load_dotenv(".env")

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    return GITHUB_TOKEN



import os
import sys
from dotenv import load_dotenv


# --------------------------------------- Function Definitions --------------------------------------- #

def verify_token():

    load_dotenv(".env")

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    if not GITHUB_TOKEN:
        return 1
    else:
        return 0


# --------------------------------------- Start of Program --------------------------------------- #

if verify_token():
    sys.exit("Failed to retrieve Github Token... Check your .env file...\nExiting")
else:
    print("Github Token Verified\nContinuing...")





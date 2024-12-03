**API Vulnerability Scraper**
-------------------------------
    Currently: Receives user input and displays to terminal
  
    TODO: 
        -check for common vulnerabilities: auth, rate limiting, etc..

        -Output to CSV? 

        -Plot something?

-------------------------------


## Installations

```
pip install -r requirements.txt
```

## DotEnv Setup

Create a file `.env` and add the following:

```
GITHUB_TOKEN=your_personal_access_token_here
```

## Run Program

Run the program to find APIs and check for any vulnerabilities:

```
py main.py
```
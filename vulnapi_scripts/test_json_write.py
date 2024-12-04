import json

data = {
    "https://collectionapi.metmuseum.org/public/collection/v1": {
        "high": [],
        "medium": [
            "CSP frame-ancestors policy is"
            "X-Frame-Options Header is" 
        ],
        "low": [],
        "info": [
            "Cookies not Secure",
            "Cookies not HTTP-Only",
            "Cookies SameSite not set",
            "Cookies not Secure",
            "Discoverable OpenAPI Path",
            "Cookies SameSite not set",
            "Cookies Expires not set",
            "CSP Header is not set",
            "Operation May Accepts",
            "CORS Allow-Origin Header is",
            "HSTS Header is missing",
            "X-Content-Type-Options Header",
            "Service Fingerprinting"
        ]
    },
    "https://collectionapi.metmuseum.org/public/collection/v2": {
        "high": [],
        "medium": [
            "CSP frame-ancestors policy is"
            "X-Frame-Options Header is" 
        ],
        "low": [],
        "info": [
            "Cookies not Secure",
            "Cookies not HTTP-Only",
            "Cookies SameSite not set",
            "Cookies not Secure",
            "Discoverable OpenAPI Path",
            "Cookies SameSite not set",
            "Cookies Expires not set",
            "CSP Header is not set",
            "Operation May Accepts",
            "CORS Allow-Origin Header is",
            "HSTS Header is missing",
            "X-Content-Type-Options Header",
            "Service Fingerprinting"
        ]
    },   
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
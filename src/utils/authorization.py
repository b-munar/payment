from functools import wraps
from flask import request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def authorization(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            header_authorization = request.headers.get("Authorization")
            if not header_authorization:
                return "", 403
            if "Bearer " not in header_authorization:
                return "", 403

            token = request.headers.get("Authorization").split(" ")[1]
            
            headers = {"Content-Type": "application/json", 
                       "Authorization": f"Bearer {token}"
                    }
            
            reqUrl = os.getenv('AUTH_HOST')+":"+os.getenv('AUTH_PORT')+os.getenv('AUTH_PATH_AUTH')
            response = requests.request("GET", reqUrl, headers=headers)
            if response.status_code == 202:
                kwargs["user"] = response.json()
                kwargs["token"] = token
                return func(*args, **kwargs)
            else:
                 return "", 401
    return decorated
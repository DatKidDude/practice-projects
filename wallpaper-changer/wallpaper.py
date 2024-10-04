import requests as req
from dotenv import dotenv_values
from pprint import pprint
import random 
import json

api_key = dotenv_values(".env")["KEY"]

# url headers
headers = {
    "Authorization": api_key,
}

parameters = {
    "query": "halloween",
    "page": 1,
    "per_page": 1,
}

# pexels api url 
url = "https://api.pexels.com/v1/search"

# send api request for photo
response = req.get(url, headers=headers, params=parameters) 

# print(pprint(response.json()))

import requests
import json

def get_eureka_response(query: str, api_key: str, user:str):
    url = "https://api.eureka-ai.co.uk/chat"
    headers = {
        "x-api-key": api_key
    }  

    data = {
        "user_id": user,
        "message": query,
    }

    response = requests.post(url, headers=headers, params=data)
    return response.json()
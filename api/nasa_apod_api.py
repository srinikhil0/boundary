import requests
import json
import webbrowser
from datetime import date
from datetime import timedelta

#API Key

API_KEY = 'a7HznUANFAIYNbYBgEZeKSHm1Umxtgoh2myhqIfO'

#API_URL

url = 'https://api.nasa.gov/planetary/apod'

#Parameters

today = date.today()
yesterday = today - timedelta(days = 1)

params = {
    'api_key':API_KEY,
    'date': yesterday,
    'hd':'True'    
}

response = requests.get(url, params=params)
json_data = json.loads(response.text)
image_url = json_data['hdurl']
webbrowser.open(image_url)
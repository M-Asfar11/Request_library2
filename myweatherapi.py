import requests
import pandas as pd 
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    'q' : "Karachi",
    'appid': api_key,
    "units" : "metric"
}

r = requests.get(url, params=params)

data = r.json()
print(data)
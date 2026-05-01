import requests
import pandas as pd 
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("api_key")
cities = ["Karachi", "Lahore", "Faisalabad", "Multan", "Islamabad", "Sialkot"]

url = "https://api.openweathermap.org/data/2.5/weather"

def weather_data(city_list):
    all_weather = []

    for city in city_list:
        params = {
            'q' : city,
            'appid': api_key,
            "units" : "metric"
        }

        try: 
            r = requests.get(url, params=params)

            if r.status_code != 200:
                print(f"Skipping: {city} not found.")
                continue

            data = r.json()
            all_weather.append(data)
            print(f"Data collected for {city}")
            
        except Exception as e:
            print(f"Error for {city}: {e}")
    return all_weather

data = weather_data(cities)
df = pd.json_normalize(data)
# df = pd.DataFrame(data)
# print(df)
print(df)
timestamp = datetime.now().strftime("%d-%m-%Y")
filename = f"weather_report_{timestamp}.csv"
# df.to_csv("weather_data_listed_cities.csv")
df.to_csv(filename, index=False)
print("file saved...")
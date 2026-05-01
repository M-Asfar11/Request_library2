import requests
import pandas as pd 
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("api_key")
cities = ["karachi", "Lahore", "Faisalabad", "Multan"]

url = "https://api.openweathermap.org/data/2.5/weather"

def weather_data(city_list):
    all_weather = []

    for city in city_list:

        params = {

            "q" : city,
            'appid': api_key,
            'units' : "metric"
        }

        try:
            
            r = requests.get(url, params=params)

            if r.status_code != 200:
                print(f"skipping: {city} not found.")
                continue

            data = r.json()

            weather_info = {
                "city" : data.get("name"),
                "temperature" : data.get("main", {}).get("temp"),
                "humidity" : data.get("main", {}).get("humidity"),
                "pressure" : data.get("main", {}).get("pressure"),
                "weather" : data.get("weather", [{}])[0].get("description"),
                "wind_speed": data.get("wind", {}).get("speed"),
                "timestamp" : datetime.now()
            }   

            all_weather.append(weather_info)

            print(f"Data collect for {city}")

        except Exception as e:
            print(f"Error for {city}: {e}")
    return all_weather

data = weather_data(cities)
df = pd.DataFrame(data)
print(df)

timestamp = datetime.now().strftime("%Y-%m-%d")
filename = f"sweather_{timestamp}.csv"

df.to_csv(filename, index=False)
print("File Saved:)")

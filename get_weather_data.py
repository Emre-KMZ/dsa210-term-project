"""
Since I was in istanbul for the interval that I will be analyzing, I will get the weather data for istanbul only.

I will use the openweathermap api to get the weather data. And save it as a csv file, to not make too many requests and exceed my free tier quota.
"""

import requests
import os
from dotenv import load_dotenv
import json


ISTANBUL_LAT = 41.0082
ISTANBUL_LON = 28.9784

def get_weather_data(start_date, end_date):
    params = {
        "latitude": ISTANBUL_LAT,
        "longitude": ISTANBUL_LON,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min,rain_sum,snowfall_sum",
        "timezone": "Europe/Istanbul"
    }
    url = "https://archive-api.open-meteo.com/v1/archive"
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    return data

if __name__ == "__main__":
    d = get_weather_data("2024-02-27", "2024-12-03")
    with open("weather_data.json", "w") as f:
        json.dump(d, f)


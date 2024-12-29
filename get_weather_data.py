"""
Since I was in istanbul for the interval that I will be analyzing, I will get the weather data for istanbul only.

I will use the openweathermap api to get the weather data. And save it as a csv file, to not make too many requests and exceed my free tier quota.
"""

import requests
import os
import json

months = {
    1: 0,
    2: 31,
    3: 59,
    4: 90,
    5: 120,
    6: 151,
    7: 181,
    8: 212,
    9: 243,
    10: 273,
    11: 304,
    12: 334
}


ISTANBUL_LAT = 41.0082
ISTANBUL_LON = 28.9784

BODRUM_LAT = 37.2749
BODRUM_LON = 27.6606

# ISTANBUL INTERVALS
# "2024-02-27" - "2024-07-25"
# "2024-07-30" - "2024-12-03"

# BODRUM INTERVALS
# "2024-07-26" - "2024-07-29"

# I was in Bodrum for 4 days in July (and my decisions are not affected by the weather in Bodrum), so I will get the weather data for Bodrum for the interval "2024-07-26" - "2024-07-29"

def get_weather_data():
    params = {
        "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min,rain_sum,snowfall_sum",
        "timezone": "Europe/Istanbul"
    }
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    # GET WEATHER DATA FOR ISTANBUL 
    params["latitude"] = ISTANBUL_LAT
    params["longitude"] = ISTANBUL_LON
    params["start_date"] = "2024-02-27"
    params["end_date"] = "2024-07-25"
    response = requests.get(url, params=params)

    data1 = response.json()

    # GET WEATHER DATA FOR BODRUM
    params["latitude"] = BODRUM_LAT
    params["longitude"] = BODRUM_LON
    params["start_date"] = "2024-07-26"
    params["end_date"] = "2024-07-29"
    response = requests.get(url, params=params)

    data2 = response.json()

    # GET WEATHER DATA FOR ISTANBUL
    params["latitude"] = ISTANBUL_LAT
    params["longitude"] = ISTANBUL_LON
    params["start_date"] = "2024-07-30"
    params["end_date"] = "2024-12-03"
    response = requests.get(url, params=params)

    data3 = response.json()
    # convert dates to single integer, similar to the format in the csv file 
    combined_daily = {
        "time": data1["daily"]["time"] + data2["daily"]["time"] + data3["daily"]["time"],
        "temperature_2m_mean": data1["daily"]["temperature_2m_mean"] + data2["daily"]["temperature_2m_mean"] + data3["daily"]["temperature_2m_mean"],
        "temperature_2m_max": data1["daily"]["temperature_2m_max"] + data2["daily"]["temperature_2m_max"] + data3["daily"]["temperature_2m_max"],
        "temperature_2m_min": data1["daily"]["temperature_2m_min"] + data2["daily"]["temperature_2m_min"] + data3["daily"]["temperature_2m_min"],
        "rain_sum": data1["daily"]["rain_sum"] + data2["daily"]["rain_sum"] + data3["daily"]["rain_sum"],
        "snowfall_sum": data1["daily"]["snowfall_sum"] + data2["daily"]["snowfall_sum"] + data3["daily"]["snowfall_sum"]
    }
    
    data = {"daily": combined_daily}

    # convert dates to single integer, similar to the format in the csv file 
    for i,d in enumerate(data["daily"]["time"]):
        data["daily"]["time"][i] = months[int(d[5:7])] + int(d[8:10])

        
    

    return data


if __name__ == "__main__":
    d = get_weather_data()
    with open("weather_data.json", "w") as f:
        json.dump(d, f)


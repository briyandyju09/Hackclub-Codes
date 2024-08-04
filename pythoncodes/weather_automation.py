import requests
from datetime import datetime
import json
import os

API_KEY = ''  
CITY = 'Dubai'  
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def get_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data")
        return None

def format_weather_data(weather_data):
    formatted_data = {
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "weather": weather_data["weather"][0]["description"],
        "humidity": weather_data["main"]["humidity"],
        "wind_speed": weather_data["wind"]["speed"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return formatted_data

def save_weather_data(formatted_data):
    file_name = f"weather_{datetime.now().strftime('%Y_%m_%d')}.json"
    if not os.path.exists("weather_logs"):
        os.makedirs("weather_logs")
    
    with open(os.path.join("weather_logs", file_name), "a") as file:
        json.dump(formatted_data, file, indent=4)
        file.write("\n")

def main():
    weather_data = get_weather_data()
    if weather_data:
        formatted_data = format_weather_data(weather_data)
        save_weather_data(formatted_data)
        print("Weather data saved successfully!")

def usage_instructions():
    print("This script fetches the current weather data for a specified city and saves it in a JSON file.")
    print("Run the script with your API key and city name configured in the script.")
    print("Example: python weather_automation.py")

if __name__ == "__main__":
    usage_instructions()
    main()

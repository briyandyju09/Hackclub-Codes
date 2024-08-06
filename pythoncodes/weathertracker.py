import requests
import schedule
import time
import logging
from datetime import datetime


API_KEY = ''
CITY_ID = '' 
THRESHOLD_TEMP = 30 
CHECK_INTERVAL = 3600 
DAILY_REPORT_TIME = "07:00"
LOG_FILE = 'weather_monitor.log'


logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_weather(city_id):
    logging.info(f"Fetching weather data for city ID: {city_id}")
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Fetched weather data: {data}")
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None


def check_weather():
    logging.info("Checking weather conditions")
    weather_data = fetch_weather(CITY_ID)
    if weather_data:
        temp = weather_data['main']['temp']
        condition = weather_data['weather'][0]['description']
        print(f"Current temperature: {temp}°C, Condition: {condition}")
        if temp > THRESHOLD_TEMP:
            notify_user(temp, condition)
        else:
            logging.info(f"Temperature {temp}°C did not cross the threshold {THRESHOLD_TEMP}°C")
    else:
        logging.warning("Could not fetch current weather data")


def notify_user(temp, condition):
    message = (f"Weather Alert: The temperature has crossed the threshold! "
               f"Current temperature: {temp}°C, Condition: {condition}")
    print(message)
    logging.info(message)



def daily_report():
    logging.info("Generating daily weather report")
    weather_data = fetch_weather(CITY_ID)
    if weather_data:
        temp = weather_data['main']['temp']
        condition = weather_data['weather'][0]['description']
        report = (f"Daily Weather Report:\n"
                  f"Temperature: {temp}°C\n"
                  f"Condition: {condition}\n")
        print(report)
        logging.info(f"Daily report generated:\n{report}")
    else:
        logging.warning("Could not fetch weather data for daily report")


def schedule_daily_report():
    schedule.every().day.at(DAILY_REPORT_TIME).do(daily_report)
    logging.info(f"Scheduled daily report at {DAILY_REPORT_TIME}")

# Main function
def main():
    print("Starting weather condition monitor...")
    logging.info("Starting weather condition monitor...")
    check_weather()  
    schedule_daily_report()
    while True:
        schedule.run_pending()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

def setup_alert_system():
    logging.info("Setting up alert system")
    pass

def check_api_status():
    logging.info("Checking API status")
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("API is reachable")
        else:
            logging.warning(f"API returned status code {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"API is not reachable: {e}")


setup_alert_system()
check_api_status()

def display_welcome_message():
    print("Welcome to the Weather Condition Monitor")
    print(f"Monitoring weather for city ID: {CITY_ID}")
    print(f"Temperature threshold set at {THRESHOLD_TEMP}°C")
    print(f"Daily report scheduled at {DAILY_REPORT_TIME}")


display_welcome_message()
logging.info("Displayed welcome message")

import requests
import time
import schedule
import logging
from datetime import datetime


API_URL = 'https://api.coingecko.com/api/v3/simple/price'
CRYPTO = 'bitcoin'
CURRENCY = 'usd'
THRESHOLD = 30000  
CHECK_INTERVAL = 60  
DAILY_CHECK_TIME = "09:00"  
LOG_FILE = 'crypto_price_tracker.log'


logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_price(crypto, currency):
    logging.info(f"Fetching price for {crypto} in {currency}")
    try:
        response = requests.get(f"{API_URL}?ids={crypto}&vs_currencies={currency}")
        response.raise_for_status()
        data = response.json()
        price = data[crypto][currency]
        logging.info(f"Fetched price: {price}")
        return price
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None


def check_price():
    logging.info("Checking price")
    current_price = fetch_price(CRYPTO, CURRENCY)
    if current_price:
        print(f"Current price of {CRYPTO} is ${current_price}")
        if current_price > THRESHOLD:
            notify_user(current_price)
        else:
            logging.info(f"Price {current_price} did not cross the threshold {THRESHOLD}")
    else:
        logging.warning("Could not fetch current price")


def notify_user(price):
    message = (f"Notification: The price of {CRYPTO} has crossed the threshold! "
               f"Current price: ${price}")
    print(message)
    logging.info(message)



def daily_check():
    schedule.every().day.at(DAILY_CHECK_TIME).do(check_price)
    logging.info(f"Scheduled daily check at {DAILY_CHECK_TIME}")


def main():
    print("Starting cryptocurrency price tracker...")
    logging.info("Starting cryptocurrency price tracker...")
    check_price() 
    daily_check()
    while True:
        schedule.run_pending()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

def setup_notifications():
    logging.info("Setting up notification system")
    pass

def check_api_status():
    logging.info("Checking API status")
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            logging.info("API is reachable")
        else:
            logging.warning(f"API returned status code {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"API is not reachable: {e}")


setup_notifications()
check_api_status()

def display_welcome_message():
    print("Welcome to the Cryptocurrency Price Tracker")
    print(f"Tracking {CRYPTO} prices in {CURRENCY}")
    print(f"Notification threshold set at ${THRESHOLD}")
    print(f"Daily check scheduled at {DAILY_CHECK_TIME}")

display_welcome_message()
logging.info("Displayed welcome message")

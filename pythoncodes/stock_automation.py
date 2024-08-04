import requests
from datetime import datetime
import json
import os

API_KEY = 'K3RDM1GH4D9JVTXZ' 
SYMBOL = 'AAPL'  
URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=5min&apikey={API_KEY}'

def get_stock_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data")
        return None

def format_stock_data(stock_data):
    time_series = stock_data.get("Time Series (5min)", {})
    latest_time = max(time_series.keys())
    latest_data = time_series[latest_time]
    
    formatted_data = {
        "symbol": SYMBOL,
        "price": latest_data["1. open"],
        "high": latest_data["2. high"],
        "low": latest_data["3. low"],
        "volume": latest_data["5. volume"],
        "timestamp": latest_time
    }
    return formatted_data

def save_stock_data(formatted_data):
    file_name = f"stock_{datetime.now().strftime('%Y_%m_%d')}.json"
    if not os.path.exists("stock_logs"):
        os.makedirs("stock_logs")
    
    with open(os.path.join("stock_logs", file_name), "a") as file:
        json.dump(formatted_data, file, indent=4)
        file.write("\n")

def main():
    stock_data = get_stock_data()
    if stock_data:
        formatted_data = format_stock_data(stock_data)
        save_stock_data(formatted_data)
        print("Stock data saved successfully!")

def usage_instructions():
    print("This script fetches the current stock data for a specified symbol and saves it in a JSON file.")
    print("Run the script with your API key and stock symbol configured in the script.")
    print("Example: python stock_automation.py")

if __name__ == "__main__":
    usage_instructions()
    main()

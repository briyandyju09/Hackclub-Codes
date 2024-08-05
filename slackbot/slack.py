from flask import Flask, request, jsonify
import os
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
import schedule
import time

app = Flask(__name__)


SLACK_BOT_TOKEN = 'xoxb-2210535565-7539728807361-WZT1jbbgwmsuGKnbKckVgTG7'
SLACK_CHANNEL_ID = 'C07E2B8P1LH'
DAILY_VERSE_TIME = "09:00"


client = WebClient(token=SLACK_BOT_TOKEN)


def fetch_random_verse():
    response = requests.get('https://bible-api.com/?random=verse')
    if response.status_code == 200:
        data = response.json()
        return f"{data['text']} - {data['reference']}"
    return "Could not fetch a verse at this time."


def send_slack_message(channel, text):
    try:
        client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")


def handle_verse_command(channel):
    verse = fetch_random_verse()
    send_slack_message(channel, verse)


def handle_findverse_command(channel, search_term):
    response = requests.get(f'https://bible-api.com/{search_term}')
    if response.status_code == 200:
        data = response.json()
        text = f"{data['text']} - {data['reference']}"
    else:
        text = "Verse not found."
    send_slack_message(channel, text)


def handle_prayreq_command(channel, request):
    send_slack_message(channel, f"Prayer request received: {request}")


def daily_verse_task():
    verse = fetch_random_verse()
    daily_message = f"Good morning! Here's your daily verse: {verse} - A great reminder for today."
    send_slack_message(SLACK_CHANNEL_ID, daily_message)


schedule.every().day.at(DAILY_VERSE_TIME).do(daily_verse_task)

@app.route('/slack/commands', methods=['POST'])
def handle_slack_commands():
    data = request.form
    command = data.get('command')
    channel = data.get('channel_id')
    text = data.get('text', '').strip()
    
    if command == '/verse':
        handle_verse_command(channel)
    elif command == '/findverse':
        if text:
            handle_findverse_command(channel, text)
        else:
            send_slack_message(channel, "Please provide a search term.")
    elif command == '/prayreq':
        if text:
            handle_prayreq_command(channel, text)
        else:
            send_slack_message(channel, "Please provide a prayer request.")
    else:
        send_slack_message(channel, "Unknown command.")
    
    return jsonify({'response_type': 'ephemeral', 'text': 'Processing your request...'})


if __name__ == "__main__":
    import threading
    

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(60)  
    
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
    

    app.run(port=3000)

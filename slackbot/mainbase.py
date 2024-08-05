import os
import requests
import json
import schedule
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime


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


def handle_command(command, channel, *args):
    if command == '/verse':
        handle_verse_command(channel)
    elif command == '/findverse':
        if args:
            handle_findverse_command(channel, ' '.join(args))
        else:
            send_slack_message(channel, "Please provide a search term.")
    elif command == '/prayreq':
        if args:
            handle_prayreq_command(channel, ' '.join(args))
        else:
            send_slack_message(channel, "Please provide a prayer request.")
    else:
        send_slack_message(channel, "Unknown command.")


def simulate_commands():

    handle_command('/verse', SLACK_CHANNEL_ID)
    handle_command('/findverse', SLACK_CHANNEL_ID, 'John 3:16')
    handle_command('/prayreq', SLACK_CHANNEL_ID, 'Please pray for my family.')

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60) 

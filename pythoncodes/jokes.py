import requests
import os
from datetime import datetime

# Constants
JOKE_API_URL = 'https://official-joke-api.appspot.com/random_joke'
OUTPUT_DIR = 'jokes'

# Function to fetch a random joke from the API
def fetch_joke():
    try:
        response = requests.get(JOKE_API_URL)
        response.raise_for_status()  # Raises an HTTPError if the response was an error
        data = response.json()
        joke = f"{data['setup']} - {data['punchline']}"
        return joke
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None

# Function to save the joke to a text file
def save_joke_to_file(joke, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"joke_{timestamp}.txt"
    filepath = os.path.join(directory, filename)

    try:
        with open(filepath, 'w') as file:
            file.write(joke)
        print(f"Joke successfully saved to {filepath}")
    except IOError as e:
        print(f"Error saving joke to file: {e}")

# Function to list all saved joke files
def list_saved_jokes(directory):
    if os.path.exists(directory):
        files = os.listdir(directory)
        if files:
            print("Saved jokes:")
            for file in files:
                print(f" - {file}")
        else:
            print("No jokes have been saved yet.")
    else:
        print(f"Directory '{directory}' does not exist.")

# Function to get the file path for the latest joke
def get_latest_joke_file(directory):
    if os.path.exists(directory):
        files = [f for f in os.listdir(directory) if f.endswith('.txt')]
        if files:
            latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
            return os.path.join(directory, latest_file)
        else:
            print("No joke files found.")
            return None
    else:
        print(f"Directory '{directory}' does not exist.")
        return None

# Function to read the latest joke from the file
def read_latest_joke(directory):
    latest_joke_file = get_latest_joke_file(directory)
    if latest_joke_file:
        try:
            with open(latest_joke_file, 'r') as file:
                return file.read()
        except IOError as e:
            print(f"Error reading joke file: {e}")
            return None
    return None

# Main function
def main():
    print("Fetching a new joke...")
    joke = fetch_joke()
    if joke:
        print("Joke fetched successfully.")
        print("Saving the joke...")
        save_joke_to_file(joke, OUTPUT_DIR)
    else:
        print("Failed to fetch a joke. No joke will be saved.")

    print("\nListing all saved jokes:")
    list_saved_jokes(OUTPUT_DIR)

    print("\nReading the latest joke:")
    latest_joke = read_latest_joke(OUTPUT_DIR)
    if latest_joke:
        print(f"Latest joke: {latest_joke}")
    else:
        print("No latest joke available.")

# Additional instructions
def additional_instructions():
    print("This script fetches a random joke, saves it to a text file with a timestamp,")
    print("and lists all saved jokes. It also reads and displays the latest saved joke.")
    print("Ensure the OUTPUT_DIR constant is set to the directory where you want to save jokes.")
    print("Example: python daily_joke_saver.py")

# Detailed steps
def detailed_steps():
    print("Detailed steps for using the script:")
    print("1. Open the script in a text editor.")
    print("2. Modify the OUTPUT_DIR constant if necessary.")
    print("3. Save the script.")
    print("4. Run the script using a Python interpreter.")
    print("5. The script will fetch a joke, save it, list all saved jokes, and display the latest joke.")

if __name__ == "__main__":
    additional_instructions()
    detailed_steps()
    main()

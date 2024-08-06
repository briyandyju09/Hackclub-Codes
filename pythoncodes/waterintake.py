import schedule
import time
import logging
from datetime import datetime


DAILY_GOAL = 2000  
REMINDER_INTERVAL = 60 
LOG_FILE = 'water_intake.log'


logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


water_intake = []


def log_water(amount):
    global water_intake
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    water_intake.append((time_now, amount))
    logging.info(f"Logged water intake: {amount}ml at {time_now}")


def display_intake():
    total_intake = sum([amount for _, amount in water_intake])
    print(f"Total water intake today: {total_intake}ml / {DAILY_GOAL}ml")
    logging.info(f"Displayed total intake: {total_intake}ml")


def water_reminder():
    print("Reminder: Don't forget to drink water!")
    logging.info("Sent reminder to drink water")


def daily_summary():
    total_intake = sum([amount for _, amount in water_intake])
    print(f"Daily Summary: You drank {total_intake}ml of water today.")
    if total_intake >= DAILY_GOAL:
        print("Congratulations! You met your daily goal.")
        logging.info("Daily goal met")
    else:
        print("You did not meet your daily goal. Try to drink more water tomorrow!")
        logging.info("Daily goal not met")


def schedule_tasks():
    schedule.every(REMINDER_INTERVAL).minutes.do(water_reminder)
    schedule.every().day.at("21:00").do(daily_summary)


def main():
    print("Welcome to the Daily Water Intake Tracker!")
    logging.info("Started Daily Water Intake Tracker")
    
    schedule_tasks()
    
    while True:
        print("\nOptions:")
        print("1. Log water intake")
        print("2. Display total intake")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                amount = int(input("Enter amount of water in ml: "))
                log_water(amount)
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == '2':
            display_intake()
        elif choice == '3':
            logging.info("Exiting Daily Water Intake Tracker")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


def setup_notification_system():
    logging.info("Setting up notification system")
    pass

def check_system_status():
    logging.info("Checking system status")
    pass


setup_notification_system()
check_system_status()

def display_welcome_message():
    print("Welcome to the Daily Water Intake Tracker!")
    print(f"Your daily goal is to drink {DAILY_GOAL}ml of water.")
    print(f"Reminders are set for every {REMINDER_INTERVAL} minutes.")
    print("Daily summary will be provided at 9 PM.")


display_welcome_message()
logging.info("Displayed welcome message")

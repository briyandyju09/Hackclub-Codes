import schedule
import time
import logging
from datetime import datetime


DAILY_REMINDER_TIME = "09:00" 
LOG_FILE = 'todo_manager.log'


logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


todo_list = []


def add_task(task):
    todo_list.append(task)
    logging.info(f"Added task: {task}")


def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        logging.info(f"Removed task: {task}")
    else:
        logging.warning(f"Task not found: {task}")


def list_tasks():
    if todo_list:
        logging.info("Listing all tasks")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
            logging.info(f"Task {idx}: {task}")
    else:
        logging.info("No tasks in the to-do list")
        print("Your to-do list is empty.")


def daily_reminder():
    logging.info("Sending daily reminder of tasks")
    print("Daily Reminder: Here are your tasks for today:")
    list_tasks()


def schedule_daily_reminder():
    schedule.every().day.at(DAILY_REMINDER_TIME).do(daily_reminder)
    logging.info(f"Scheduled daily reminder at {DAILY_REMINDER_TIME}")


def main():
    print("Welcome to the To-Do List Manager!")
    logging.info("Started To-Do List Manager")
    schedule_daily_reminder()
    
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. List all tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            logging.info("Exiting To-Do List Manager")
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
    print("Welcome to the To-Do List Manager!")
    print("You can add, remove, and list tasks.")
    print(f"Daily reminder scheduled at {DAILY_REMINDER_TIME}")


display_welcome_message()
logging.info("Displayed welcome message")

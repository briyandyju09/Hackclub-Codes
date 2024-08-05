import psutil
import schedule
import time
import logging
from datetime import datetime


CHECK_INTERVAL = 3600  
DAILY_REPORT_TIME = "18:00"  
DISK_THRESHOLD = 10  
LOG_FILE = 'disk_space_monitor.log'


logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


def check_disk_space():
    logging.info("Checking disk space")
    disk = psutil.disk_usage('/')
    free_gb = disk.free / (1024 ** 3)
    
    logging.info(f"Free disk space: {free_gb:.2f} GB")
    print(f"Free disk space: {free_gb:.2f} GB")
    
    if free_gb < DISK_THRESHOLD:
        alert_user(free_gb)
    else:
        logging.info(f"Disk space is above the threshold of {DISK_THRESHOLD} GB")


def alert_user(free_gb):
    message = (f"Alert: Available disk space is below the threshold! "
               f"Current free space: {free_gb:.2f} GB")
    print(message)
    logging.warning(message)
   


def daily_report():
    logging.info("Generating daily disk space report")
    disk = psutil.disk_usage('/')
    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)
    
    report = (f"Daily Disk Space Report:\n"
              f"Total: {total_gb:.2f} GB\n"
              f"Used: {used_gb:.2f} GB\n"
              f"Free: {free_gb:.2f} GB\n")
    
    print(report)
    logging.info(f"Daily report generated:\n{report}")


def schedule_daily_report():
    schedule.every().day.at(DAILY_REPORT_TIME).do(daily_report)
    logging.info(f"Scheduled daily report at {DAILY_REPORT_TIME}")



def main():
    print("Starting disk space monitor...")
    logging.info("Starting disk space monitor...")
    check_disk_space()  
    schedule_daily_report()
    
    while True:
        schedule.run_pending()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

def setup_alert_system():
    logging.info("Setting up alert system")

    pass

def check_system_status():
    logging.info("Checking system status")
    pass

setup_alert_system()
check_system_status()

def display_welcome_message():
    print("Welcome to the Disk Space Monitor")
    print(f"Disk space threshold set at {DISK_THRESHOLD} GB")
    print(f"Daily report scheduled at {DAILY_REPORT_TIME}")


display_welcome_message()
logging.info("Displayed welcome message")

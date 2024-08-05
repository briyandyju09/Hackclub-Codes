import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os

# Email Credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient_email@gmail.com'

# Function to prompt user for tasks and save to a file
def prompt_tasks():
    tasks = []
    print("Enter your tasks for today. Type 'done' when finished:")
    while True:
        task = input("Task: ")
        if task.lower() == 'done':
            break
        tasks.append(task)

    with open('daily_tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")
    return tasks

# Function to read tasks from file
def read_tasks():
    if os.path.exists('daily_tasks.txt'):
        with open('daily_tasks.txt', 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    else:
        return []

# Function to create an email
def create_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

# Function to send an email
def send_email(msg):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to get the email content
def get_email_content(tasks):
    subject = "Daily To-Do List"
    body = f"Hello,\n\nHere is your to-do list for today ({datetime.now().strftime('%Y-%m-%d')}):\n\n"
    for i, task in enumerate(tasks, 1):
        body += f"{i}. {task}\n"
    body += "\nBest regards,\nYour To-Do List Bot"
    return subject, body

# Main function
def main():
    tasks = prompt_tasks()
    if tasks:
        subject, body = get_email_content(tasks)
        msg = create_email(subject, body)
        send_email(msg)
    else:
        print("No tasks entered.")

# Usage instructions
def usage_instructions():
    print("This script generates a daily to-do list and sends it to your email.")
    print("Configure your email credentials in the script.")
    print("Example: python daily_todo_email.py")

# Additional instructions
def additional_instructions():
    print("Make sure you have enabled 'less secure app access' for your email account if using Gmail.")
    print("You can customize the email content by modifying the get_email_content() function.")
    print("To automate this script, use a task scheduler like cron (Linux) or Task Scheduler (Windows).")

# Detailed steps
def detailed_steps():
    print("Detailed steps for using the script:")
    print("1. Open the script in a text editor.")
    print("2. Replace 'your_email@gmail.com' and 'your_password' with your email credentials.")
    print("3. Replace 'recipient_email@gmail.com' with the recipient's email address.")
    print("4. Save the script.")
    print("5. Run the script using a Python interpreter.")
    print("6. Verify the email is received in the recipient's inbox.")

if __name__ == "__main__":
    usage_instructions()
    additional_instructions()
    detailed_steps()
    main()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient_email@gmail.com'

def create_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

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

def get_email_content():
    subject = "Daily Reminder"
    body = f"""
    Hello,

    This is your daily reminder.

    Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

    Here's a motivational quote for today:
    "The only way to do great work is to love what you do." - Steve Jobs

    Your tasks for today:
    1. Check emails.
    2. Attend team meeting at 10 AM.
    3. Work on project X.
    4. Review pull requests.

    Don't forget to take breaks and stay hydrated!

    Best regards,
    Your Automated Reminder
    """
    return subject, body

def main():
    subject, body = get_email_content()
    msg = create_email(subject, body)
    send_email(msg)

def usage_instructions():
    print("This script sends a daily reminder email.")
    print("Configure your SMTP server, email address, and password in the script.")
    print("Example: python daily_reminder.py")

def additional_instructions():
    print("Make sure you have enabled 'less secure app access' for your email account if using Gmail.")
    print("You can customize the email content by modifying the get_email_content() function.")
    print("To automate this script, use a task scheduler like cron (Linux) or Task Scheduler (Windows).")

if __name__ == "__main__":
    usage_instructions()
    additional_instructions()
    main()
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Email credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient_email@gmail.com'

# API call
def fetch_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data['content']
        author = quote_data['author']
        return f'"{quote}"\n\n- {author}'
    else:
        return "Failed to fetch quote"

# Create email
def create_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

# Send email
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

# Body of the email
def get_email_content():
    quote = fetch_quote()
    subject = "Daily Motivational Quote"
    body = f"Hello,\n\nHere is your motivational quote for today ({datetime.now().strftime('%Y-%m-%d')}):\n\n{quote}\n\nBest regards,\nYour Motivation Bot"
    return subject, body

# Main function
def main():
    subject, body = get_email_content()
    msg = create_email(subject, body)
    send_email(msg)

# Usage instructions
def usage_instructions():
    print("This script fetches a random motivational quote and sends it to your email.")
    print("Configure your email credentials in the script.")
    print("Example: python daily_quote_email.py")

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

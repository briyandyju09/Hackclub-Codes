import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

NEWS_API_KEY = ''
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient_email@gmail.com'

def fetch_news():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        return news_data['articles']
    else:
        print("Failed to fetch news")
        return []

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

def get_email_content(articles):
    subject = "Daily News Update"
    body = f"Hello,\n\nHere are the latest news headlines for today ({datetime.now().strftime('%Y-%m-%d')}):\n\n"
    for article in articles:
        body += f"Title: {article['title']}\n"
        body += f"Description: {article['description']}\n"
        body += f"URL: {article['url']}\n\n"
    body += "Best regards,\nYour News Bot"
    return subject, body

def main():
    articles = fetch_news()
    if articles:
        subject, body = get_email_content(articles)
        msg = create_email(subject, body)
        send_email(msg)

def usage_instructions():
    print("This script fetches the latest news headlines and sends them to your email.")
    print("Configure your News API key, SMTP server, email address, and password in the script.")
    print("Example: python daily_news_email.py")

def additional_instructions():
    print("Make sure you have enabled 'less secure app access' for your email account if using Gmail.")
    print("You can customize the email content by modifying the get_email_content() function.")
    print("To automate this script, use a task scheduler like cron (Linux) or Task Scheduler (Windows).")

def detailed_steps():
    print("Detailed steps for using the script:")
    print("1. Open the script in a text editor.")
    print("2. Replace 'your_news_api_key_here' with your News API key.")
    print("3. Replace 'your_email@gmail.com' and 'your_password' with your email credentials.")
    print("4. Replace 'recipient_email@gmail.com' with the recipient's email address.")
    print("5. Save the script.")
    print("6. Run the script using a Python interpreter.")
    print("7. Verify the email is received in the recipient's inbox.")

if __name__ == "__main__":
    usage_instructions()
    additional_instructions()
    detailed_steps()
    main()
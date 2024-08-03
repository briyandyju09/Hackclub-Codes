import pandas as pd
import datetime
import smtplib
import time
import requests
from win10toast import ToastNotifier

GMAIL_ID = 'your_email_here'
GMAIL_PWD = 'your_password_here'

toast = ToastNotifier()

def send_email(recipient, subject, message):
    with smtplib.SMTP('smtp.gmail.com', 587) as gmail:
        gmail.starttls()
        gmail.login(GMAIL_ID, GMAIL_PWD)
        gmail.sendmail(GMAIL_ID, recipient, f"Subject: {subject}\n\n{message}")
    print(f"Email sent to {recipient} with subject '{subject}' and message: {message}")
    toast.show_toast("Email Sent!", f"{recipient} has been emailed", duration=6)

def send_sms(recipient_number, message, sender_name, subject):
    url = "https://www.fast2sms.com/dev/bulk"
    payload = f"sender_id=FSTSMS&message={message}&language=english&route=p&numbers={recipient_number}"
    headers = {
        'authorization': "API_KEY_HERE",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    print(f"SMS sent to {recipient_number} with subject '{subject}' and message: {message}")
    toast.show_toast("SMS Sent!", f"{sender_name} has been messaged", duration=6)

if __name__ == "__main__":
    df = pd.read_excel("excelsheet.xlsx")

    today_date = datetime.datetime.now().strftime("%d-%m")
    current_year = datetime.datetime.now().strftime("%Y")

    indices_to_update = []

    for idx, row in df.iterrows():
        message = f"Many happy returns of the day, dear {row['NAME']}!"
        birthday = row['Birthday'].strftime("%d-%m")

        if today_date == birthday and current_year not in str(row['Year']):
            send_email(row['Email'], "Happy Birthday!", message)
            send_sms(row['Contact'], message, row['NAME'], "Happy Birthday!")
            indices_to_update.append(idx)

    for idx in indices_to_update:
        df.at[idx, 'Year'] = f"{df.at[idx, 'Year']},{current_year}"

    df.to_excel('excelsheet.xlsx', index=False)
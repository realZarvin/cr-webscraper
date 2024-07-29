#Start of sending Emails

import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#Email Configuration;

SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587 
EMAIL = 'midasscanner@gmail.com'  # Sending Email, Var?
PASSWORD = 'Melo2006.'  # Password


# Email list;

email_list = pd.read_csv('emails.csv')


# Email parts with variations

headings = [
    "Dear {recipient},",
    "Hello {recipient},",
    "Hi {recipient},",
    "Greetings {recipient},",
    "Hey {recipient},"
]

introductions = [
    "I hope this message finds you well. My name is Zarvin, and I am a Community Manager at BitMart.",
    "I trust you are doing great. My name is Zarvin, and I am the Community Manager at BitMart.",
    "I hope all is well with you. I'm Zarvin, the Community Manager at BitMart.",
    "I hope this email finds you in good spirits. My name is Zarvin, Community Manager at BitMart.",
    "I hope you're having a good day. I'm Zarvin, and I manage the community at BitMart."
]

ctas = [
    "We are confident that your project will thrive on our platform, reaching new heights and attracting a broader community of supporters. If you are interested in exploring this opportunity, please reply to this email. I would be delighted to provide you with further details and assist you with the listing process.",
    "We believe your project will excel on our platform, gaining new heights and attracting a larger community of supporters. If you are interested in this opportunity, please reply to this email. I would be happy to provide more details and help you with the listing process.",
    "We are sure that your project will flourish on our platform, achieving new milestones and attracting a wider community of supporters. If you are interested in this opportunity, please reply to this email. I would love to give you more information and assist you with the listing process.",
    "We are confident your project will succeed on our platform, reaching new levels and gaining a broader community of supporters. If you are interested in this opportunity, please reply to this email. I would be thrilled to provide more details and assist you with the listing process.",
    "We believe your project will thrive on our platform, attaining new heights and drawing a larger community of supporters. If you are interested in this opportunity, please reply to this email. I would be eager to provide more details and assist you with the listing process."
]


# Function to send email

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    
    
    msg.attach(MIMEText(body, 'plain'))
    
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, to_email, msg.as_string())
            print(f'Email sent to {to_email}')
    except Exception as e:
        print(f'Failed to send email to {to_email}: {e}')


# Send emails with random combinations of the email parts

for index, row in email_list.iterrows():
    recipient_email = row['email']
    heading = random.choice(headings).format(recipient=recipient_email)
    introduction = random.choice(introductions)
    cta = random.choice(ctas)
    body = f"{heading}\n\n{introduction}\n\n{cta}\n\nBest regards,\nZarvin\nCommunity Manager\nBitMart\nzarvinns@gmail.com"
    send_email(recipient_email, subject, body)


#End of Programming 

# app/utils/email_sender.py
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_verification_email(to_email: str, code: str):
    """
    Send a verification email with the code to the given email address.
    Returns True if successful, False otherwise.
    """
    try:
        msg = MIMEText(f"Your verification code is: {code}")
        msg['Subject'] = "Aditya OSINT Verification Code"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("✅ Email sent successfully")
        return True
    except Exception as e:
        print("❌ Email send failed:", e)
        return False


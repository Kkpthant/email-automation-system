import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import re
import pyotp
import logging

# Load environment variables from .env
load_dotenv()

EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')

if not EMAIL_SENDER or not EMAIL_PASSWORD:
    raise ValueError("Missing credentials! Ensure .env file is correctly configured.")

# Setup logging
logging.basicConfig(filename='email_activity.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Generate OTP for 2FA
otp_secret = pyotp.random_base32()
totp = pyotp.TOTP(otp_secret)
otp = totp.now()

# Request OTP verification
user_otp = input(f"Enter the OTP sent to your registered device (Generated OTP: {otp} for testing): ")
if user_otp != otp:
    logging.warning("Unauthorized OTP entry attempt!")
    print("Invalid OTP. Access denied.")
    exit()

# Email content
subject = "Automated Email with Python SMTP"
body = """Hello,

This is an test email sent via Python script with Gmail SMTP & App Pwd.

Best,
Python Email Bot
"""

# Phishing detection function
def is_phishing_email(body):
    phishing_patterns = [
        r'\bpassword\b', r'\bcredit card\b', r'\bbank account\b',
        r'\burgent\b', r'\bclick here\b', r'\bverify\b',
        r'\blogin\b', r'\bupdate your account\b'
    ]
    suspicious_links = [r'bit\.ly', r'tinyurl\.com', r'goo\.gl']

    # Debugging output
    print("Checking email body:", body)

    for pattern in phishing_patterns:
        if re.search(pattern, body, re.IGNORECASE):
            print(f"⚠️ Found phishing keyword: {pattern}")
            return True  # Phishing detected

    for link in suspicious_links:
        if re.search(link, body, re.IGNORECASE):
            print(f"⚠️ Found suspicious link: {link}")
            return True  # Phishing detected

    return False  # Safe email

# Check phishing before sending
if is_phishing_email(body):
    logging.warning("⚠️ Phishing attempt detected! Email not sent.")
    print("Phishing content detected. Email blocked for security.")
    exit()

# Prepare email
em = EmailMessage()
em['From'] = EMAIL_SENDER
em['To'] = EMAIL_RECEIVER
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# Send email using Gmail SMTP with App Password
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())

    logging.info("Email successfully sent to %s", EMAIL_RECEIVER)
    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError:
    logging.error("Failed to authenticate with Gmail SMTP. Check credentials.")
    print("Authentication failed. Please check your email credentials.")
except Exception as e:
    logging.error("Email sending failed: %s", str(e))
    print(f"Failed to send email: {e}")

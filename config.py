from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Twilio konfiguracija
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  # acc sid
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")  # auth token
TWILIO_SMS_API_URL = os.getenv("TWILIO_SMS_API_URL")  # api url
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # verifikovan twilio broj telefona +38160123123
import smtplib
import requests
from twilio.rest import Client
from config import SMTP_SERVER, SMTP_PORT, EMAIL_USERNAME, EMAIL_PASSWORD, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

# Funkcija za slanje ključa putem email-a.
def send_via_email(recipient_email, key):
    """ 
    Ova funkcija šalje ključ na zadatu email adresu koristeći SMPT protokol.
    Uspostavlja konekciju, aktivira TLS enkripciju, autentifike se pomoću kredencija definisanih u config.py, formira email poruku sa naslovom i telom, i na kraju šalje poruku.

    """
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            subject = "Vac kljuc"
            message = f"Subject: {subject}\n\nVac kljuc je: {key}"
            server.sendmail(EMAIL_USERNAME, recipient_email, message)
        return True, "Uspesno."
    except Exception as e:
        return False, str(e)


# Slanje SMS poruke koristeći Twilio API.
def send_via_sms(recipient_phone, message):
    """ 
    Ova funkcija šalje SMS poruku na zadati broj telefona koristeći Twilio API.
    Kreira Twilio klijent koristeći SID i AUTH token iz config.py, zatim formira i šalje SMS poruku sa 
    zadatim telom poruke i brojem primaoca, ako je uspešno slanje prikazuje SID poruke u konzoli, a
    u slučaju greške vraća None i ispisuje poruku o grešci.

    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_="", # broj telefona sa kojeg se salju poruke, a koju dodeljuje twilio +12345678901
            to=recipient_phone
        )
        print(f"Poruka je uspešno poslata. SID: {message.sid}")
        return message.sid
    except Exception as e:
        print(f"Neuspešno slanje SMS poruke: {e}")
        return None


"""
Ovaj Python kod predstavlja alat za deljenje ključeva putem više kanala, koristeći Shamir's Secret Sharing (SSS) 
algoritam za deljenje enkriptovanog ključa na više delova, koji se zatim šalju različitim kanalima (email, SMS, QR kod). 
Ključ se može rekonstruisati samo kombinovanjem sva tri dela.

### Funkcionalnosti:
1. Generisanje i validacija kriptografskih ključeva.
2. Enkripcija ključeva pomoću Fernet metode.
3. Deljenje ključa na tri dela koristeći SSS algoritam.
4. Slanje delova ključa putem:
   - Email-a (SMTP protokol),
   - SMS-a (Twilio API),
   - QR koda (generisan i sačuvan u fajlu).
5. Rekonstrukcija originalnog ključa iz tri odvojena dela.

### Tehnologije i biblioteke:
- cryptography za generisanje i enkripciju ključeva.
- secretsharing za mplementaciju Shamir's Secret Sharing algoritma.
- smtplib za slanje email poruka.
- Twilio API za slanje SMS poruka.
- qrcode za generisanje QR koda.
- secrets i string za bezbedno generisanje nasumičnih ključeva.
"""

from secretsharing import SecretSharer
import qrcode
from key_generation import generate_key, validate_key
from channel_communication import send_via_email, send_via_sms
from encryption_utils import generate_encryption_key, encrypt_key, decrypt_key
from utils import log_message, handle_error


def send_keys():
    log_message("Dobrodošli u alat za deljenje ključeva!")
    # Izbor između unosa sopstvenog ključa ili generisanja nasumičnog ključa
    choice = input("Izaberite opciju:\n1. Unesite sopstveni ključ\n2. Generišite nasumičan ključ\nUnesite broj opcije: ")

    if choice == '1':
        key = input("Unesite sopstveni ključ: ")
        is_valid, validation_message = validate_key(key)
        if not is_valid:
            # Greška u validaciji ključa (npr. prekratak)
            handle_error(validation_message)
            return
    elif choice == '2':
        # Korak 1: Generisanje ključa
        key = generate_key()
        log_message(f"Generisani ključ: {key}")
    else:
        handle_error("Nevažeća opcija.")
        return

    # Korak 2: Generisanje enkripcionog ključa i enkripcija originalnog ključa
    encryption_key = generate_encryption_key()
    encrypted_key = encrypt_key(key, encryption_key)
    log_message(f"Enkriptovani ključ: {encrypted_key}")

    # Čuvanje enkripcionog ključa u fajlu za kasniju upotrebu
    with open("encryption_key.txt", "wb") as key_file:
        key_file.write(encryption_key)
    log_message("Enkripcioni ključ je sačuvan u fajlu 'encryption_key.txt'.")

    # Korak 3: Deljenje ključa na 3 dela koristeći Shamir's Secret Sharing
    encrypted_key_hex = encrypted_key.hex()
    shares = SecretSharer.split_secret(encrypted_key_hex, 3, 3)
    email_share, sms_share, qr_share = shares

    # Korak 4: Slanje prvog i drugog dela ključa
    email_recipient = input("Unesite email primaoca: ")
    sms_recipient = input("Unesite broj telefona primaoca: ")

    email_success, email_message = send_via_email(email_recipient, email_share)
    
    sms_result = send_via_sms(sms_recipient, sms_share)
    if sms_result is None:
        handle_error("Slanje SMS-a nije uspelo.")
        sms_success = False
        sms_message = "Slanje SMS-a nije uspelo."
    else:
        sms_success = True
        sms_message = sms_result

    # Korak 5: Generisanje QR koda za treći deo ključa i čuvanje u fajl
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_share)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("key_share_qr.png")
    log_message("QR kod za treći deo ključa je generisan i sačuvan kao 'key_share_qr.png'.")

    # Završni rezultat
    if email_success and sms_success:
        log_message("Ključ je uspešno podeljen putem email-a, SMS-a i QR koda.")
    else:
        if not email_success:
            handle_error(email_message)
        if not sms_success:
            handle_error(sms_message)


def decode_keys():
    # Korak 6: Prikupljanje delova ključa od korisnika
    received_email_share = input("Unesite deo ključa primljen putem email-a: ")
    received_sms_share = input("Unesite deo ključa primljen putem SMS-a: ")
    qr_share = input("Unesite deo ključa iz QR koda: ")
    encryption_key = input("Unesite enkripcioni ključ: ")

    try:
        # Rekonstrukcija originalnog ključa iz delova
        recovered_key_hex = SecretSharer.recover_secret([received_email_share, received_sms_share, qr_share])
        recovered_key = bytes.fromhex(recovered_key_hex)
        # Dekodiranje rekonstruisanog ključa pomoću enkripcionog ključa
        decrypted_key = decrypt_key(recovered_key, encryption_key.encode())
        log_message(f"Dekodirani ključ: {decrypted_key}")
    except Exception as e:
        handle_error(f"Greška prilikom oporavka i dekodiranja ključa: {e}")


def main():
    # Glavni meni
    while True:
        print("Izaberite opciju:")
        print("1. Slanje ključeva")
        print("2. Dekodiranje dobijenih ključeva")
        print("3. Izlaz")
        choice = input("Unesite broj opcije: ")

        if choice == '1':
            # Pokretanje procesa za slanje ključeva
            send_keys()
        elif choice == '2':
            # Pokretanje procesa za dekodiranje ključeva
            decode_keys()
        elif choice == '3':
            print("Izlaz iz programa.")
            break
        else:
            print("Nevažeća opcija, pokušajte ponovo.")

if __name__ == "__main__":
    main()
from cryptography.fernet import Fernet

# Generisanje Fernet ključa
def generate_encryption_key():
    """
    Ova funkcija generiše nasumičan Fernet ključ za enkripciju.
    Generiše sigurni ključ i vraća generisani ključ u bajt formatu.

    """
    return Fernet.generate_key() 

# Enkripcija ključa koristeći Fernet
def encrypt_key(key, encryption_key):
    """
    Ova funkcija koristi Fernet enkripciju za šifrovanje zadanog ključa.
    Inicijalizuje fernet instancu koristeći dostavljeni enkripcioni ključ, pretvara zadati ključ u bajtove, šifruje ključ i vraća šifrovani ključ u bajt formatu.

    """
    fernet = Fernet(encryption_key)
    return fernet.encrypt(key.encode())

# Dekodiranje
def decrypt_key(encrypted_key, encryption_key):
    """
    Ova funkcija dešifruje šifrovani ključ koristeći Fernet.
    Inicijalizuje `Fernet` instancu koristeći dostavljeni enkripcioni ključ, koristi `Fernet.decrypt()` metodu za dešifrovanje šifrovanog ključa, pretvara dešifrovane bajtove nazad u string pomoću `decode()` metode i vraća originalni ključ u obliku stringa.

    """
    fernet = Fernet(encryption_key)
    return fernet.decrypt(encrypted_key).decode()
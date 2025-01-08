import secrets
import string

def generate_key(length=32): # 32 bajta = 256 bita
    """
    Generiše nasumičan ključ zadate dužine koristeći siguran generator slučajnih brojeva.
    Definiše skup karaktera koji se mogu koristiti u ključu i nasumično bira karaktere iz tog skupa,
    formirajući string zadate dužine.

    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def validate_key(key):
    """
    Proverava da li zadati ključ zadovoljava osnovne kriterijume validecije, a to da li je ključ duži od minimalne dužine (16 karaktera), ako nije vraća grešku, u suprotnom vraća poruku o uspešnoj validaciji.

    """
    if len(key) < 16:
        return False, "Ključ je prekratak."
    return True, "Ključ je validan"

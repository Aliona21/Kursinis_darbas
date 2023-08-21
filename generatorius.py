# Importuojame reikiamas bibliotekas
import string
import random

# Funkcija, kuri generuoja sąrašą specialių simbolių ir tikrina, ar slaptažodis atitinka reikalavimus
def slaptazodziu_generatorius(ilgis):
    simboliai = string.ascii_letters + string.digits + string.punctuation
    while True:
        slaptazodis = ''.join(random.choice(simboliai) for _ in range(ilgis))
        # Tikriname, ar slaptažodyje yra bent vienas skaičius, mažoji raidė, didžioji raidė ir specialus simbolis
        if (any(c.isdigit() for c in slaptazodis) and
            any(c.islower() for c in slaptazodis) and
            any(c.isupper() for c in slaptazodis) and
            any(c in string.punctuation for c in slaptazodis)):
            return slaptazodis

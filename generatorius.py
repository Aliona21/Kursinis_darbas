import string
import random

def slaptazodziu_generatorius(ilgis):
    simboliai = string.ascii_letters + string.digits + string.punctuation
    while True:
        slaptazodis = ''.join(random.choice(simboliai) for _ in range(ilgis))
        if (any(c.isdigit() for c in slaptazodis) and
            any(c.islower() for c in slaptazodis) and
            any(c.isupper() for c in slaptazodis) and
            any(c in string.punctuation for c in slaptazodis)):
            return slaptazodis
# Importuojame reikiamas bibliotekas
import tkinter
from tkinter import messagebox
import generatorius
import logging

# Konfigūruojame pasirinktą lygį žurnaliavimui į failą
logging.basicConfig(filename='slaptazodziai.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Funkcija, kuri generuoja slaptažodžius pagal nurodytą kiekį ir ilgį
def generuoti_slaptazodzius():
    try:
        slaptazodziu_kiekis = int(kiekis.get())
    except ValueError:
        messagebox.showerror("Klaida", "Neteisingas kiekis")
        return

    try:
        slaptazodzio_ilgis = int(ilgis.get())
        # Tikriname, ar slaptažodžio ilgis yra tarp 8 ir 127 simbolių
        if slaptazodzio_ilgis < 8:
            messagebox.showwarning("Klaida", "Įvestas slaptažodžio ilgis per trumpas")
            return
        elif slaptazodzio_ilgis > 127:
            messagebox.showwarning("Klaida", "Įvestas slaptažodžio ilgis per ilgas")
            return
    except ValueError:
        messagebox.showerror("Klaida", "Neteisingas ilgis")
        return

    nauji_slaptazodziai = []
    for _ in range(slaptazodziu_kiekis):
        slaptazodis = generatorius.slaptazodziu_generatorius(slaptazodzio_ilgis)
        logging.info('Sukurtas naujas slaptazodis')
        nauji_slaptazodziai.append(slaptazodis)
        logging.info('Naujas slaptazodis pridetas i faila')

    # Įrašome naujus slaptažodžius į failą
    with open('slaptazodziai.txt', 'a') as failas:
        failas.write('\n'.join(nauji_slaptazodziai) + '\n')

    sugeneruoti = "\n".join(nauji_slaptazodziai)
    # Sukuriame naują langą su sugeneruotais slaptažodžiais
    slaptazodziai_langas = tkinter.Toplevel(langas)
    slaptazodziai_langas.title("Sugeneruoti slaptažodžiai")
    tkinter.Label(slaptazodziai_langas, text="Jūsų sugeneruoti slaptažodžiai:").pack()
    tkinter.Label(slaptazodziai_langas, text=sugeneruoti).pack()
    tkinter.Label(slaptazodziai_langas, text="Slaptažodžiai pridėti į failą 'slaptazodziai.txt'.").pack()

# Funkcija, kuri rodo esamus slaptažodžius iš failo
def rodyti_slaptazodzius():
    try:
        with open('slaptazodziai.txt', 'r') as failas:
            slaptazodziai = failas.read()
            slaptazodziai_langas = tkinter.Toplevel(langas)
            slaptazodziai_langas.title("Slaptažodžių sąrašas")
            tkinter.Label(slaptazodziai_langas, text=slaptazodziai).pack()
    except FileNotFoundError:
        messagebox.showerror("Klaida", "Failas slaptazodziai.txt nerastas")

# Funkcija, kuri išeina iš programos
def iseiti():
    if messagebox.askyesno("Išeiti", "Ar tikrai norite išeiti?"):
        langas.destroy()

# Sukuriame pagrindinį langą
langas = tkinter.Tk()
langas.title("Slaptažodžių Generatorius")
langas.geometry("320x200")

# Sveikinimo ir nustatymų įvedimo laukai bei mygtukai
pasveikinimas = tkinter.Label(langas, text="Sveiki. Ši programa generuoja sunkius slaptažodžius\nir įrašo juos į failą slaptazodziai.txt")
pasveikinimas.pack()

kiekis = tkinter.Entry(langas)
tkinter.Label(langas, text="Įveskite kiek slaptažodžių norite sugeneruoti:").pack()
kiekis.pack()

ilgis = tkinter.Entry(langas)
tkinter.Label(langas, text="Įveskite norimą slaptažodžių ilgį:").pack()
ilgis.pack()

mygtukas_generuoti = tkinter.Button(langas, text="Generuoti slaptažodžius", command=generuoti_slaptazodzius)
mygtukas_generuoti.pack()

mygtukas_sarasas = tkinter.Button(langas, text="Rodyti slaptažodžių sarašą", command=rodyti_slaptazodzius)
mygtukas_sarasas.pack()

mygtukas_iseiti = tkinter.Button(langas, text="Išeiti", command=iseiti)
mygtukas_iseiti.pack()

# Paleidžiame pagrindinį GUI (grafinį vartotojo sąsajos) langą
langas.mainloop()

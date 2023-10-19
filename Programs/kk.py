import os
import pyautogui
import keyboard
import tkinter as tk
from tkinter import ttk
from threading import Thread

# Képernyőkép mentési mappája
mentesi_mappa = 'Képernyőképek'

# Ha a mappa nem létezik, hozd létre
if not os.path.exists(mentesi_mappa):
    os.makedirs(mentesi_mappa)

# Azonosító a képernyőképekhez
kezdo_azonosito = 1

# A fő ablak létrehozása
root = tk.Tk()
root.title("Képernyőkép Készítő")

# Képernyőkép készítés funkció
def keszit_kepernyokepet():
    global kezdo_azonosito
    while True:
        keyboard.wait('right')
        kep = pyautogui.screenshot()
        fajlnev = f'img_{kezdo_azonosito}.png'
        kep.save(os.path.join(mentesi_mappa, fajlnev))
        kezdo_azonosito += 1

# A háttérfolyamat indítása
keszito_folyamat = Thread(target=keszit_kepernyokepet)
keszito_folyamat.daemon = True
keszito_folyamat.start()

# Képernyőkép készítés gomb
gomb_kep = ttk.Button(root, text="Képernyőkép Készítés")
gomb_kep.pack()

# Kilépés gomb
gomb_kilep = ttk.Button(root, text="Kilépés", command=root.destroy)
gomb_kilep.pack()

# A GUI futtatása
root.mainloop()
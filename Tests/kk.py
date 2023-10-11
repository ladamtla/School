import os
import pyautogui
import keyboard

# A képernyőkép mentési mappája
mentesi_mappa = 'Képernyőképek'

# Ügyelj arra, hogy a mappa létezik-e, és ha nem, hozd létre
if not os.path.exists(mentesi_mappa):
    os.makedirs(mentesi_mappa)

# Azonosító, amelyet hozzáadunk a képernyőkép nevéhez
kezdo_azonosito = 1

# Képernyőkép készítése és mentése, amikor megnyomod a jobbra mutató nyilat
while True:
    # Várunk, amíg a jobbra mutató nyilat meg nem nyomod
    keyboard.wait('right')

    # Képernyőkép elkészítése
    kep = pyautogui.screenshot()

    # A képernyőkép fájlneve
    fajlnev = f'img_{kezdo_azonosito}.png'

    # A képernyőkép mentése a mappába
    kep.save(os.path.join(mentesi_mappa, fajlnev))

    # Azonosító növelése a következő képernyőképhez
    kezdo_azonosito += 1
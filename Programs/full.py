import os
import pyautogui
import tkinter as tk
from tkinter import ttk
from threading import Thread
from pynput import keyboard
from PyPDF2 import PdfFileWriter, PdfReader
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from PIL import Image

# Képernyőkép mentési mappája
mentesi_mappa = 'Képernyőképek'

# PDF fájl neve, amibe az összefűzött képek kerülnek
pdf_file = "osszefuzott.pdf"

# Azonosító a képernyőképekhez
kezdo_azonosito = 1
keszit_kepernyokepet_folytatodik = True

# Ha a mappa nem létezik, hozd létre
if not os.path.exists(mentesi_mappa):
    os.makedirs(mentesi_mappa)

# Képernyőkép készítés funkció
def keszit_kepernyokepet():
    global kezdo_azonosito, keszit_kepernyokepet_folytatodik
    while keszit_kepernyokepet_folytatodik:
        print("Képernyőkép készítése...")
        kep = pyautogui.screenshot()
        fajlnev = f'{mentesi_mappa}/img_{kezdo_azonosito}.png'
        kep.save(fajlnev)
        kezdo_azonosito += 1

# PDF-generálás funkció
def generalt_pdf():
    global keszit_kepernyokepet_folytatodik
    keszit_kepernyokepet_folytatodik = False  # Leállítjuk a képernyőkép készítést
    print("PDF generálása...")

    file_names = [file for file in os.listdir(mentesi_mappa) if file.lower().endswith('.png')]

    if not file_names:
        print("Nincs PNG fájl a megadott mappában.")
        return

    file_names.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

    c = canvas.Canvas(pdf_file, pagesize=landscape(A4))
    output_pdf = PdfFileWriter()

    for file_name in file_names:
        image = Image.open(os.path.join(mentesi_mappa, file_name))
        pdf_width, pdf_height = landscape(A4)

        img_width, img_height = image.size
        aspect_ratio = img_width / img_height

        if aspect_ratio > 1:
            new_width = pdf_width
            new_height = pdf_width / aspect_ratio
        else:
            new_height = pdf_height
            new_width = pdf_height * aspect_ratio

        x_offset = (pdf_width - new_width) / 2
        y_offset = (pdf_height - new_height) / 2

        c.drawImage(os.path.join(mentesi_mappa, file_name), x_offset, y_offset, width=new_width, height=new_height)
        c.showPage()

    c.save()

    print(f'A(z) {pdf_file} fájl elkészült.')

# Fő ablak létrehozása
root = tk.Tk()
root.title("Képernyőkép Készítő")

# Képernyőkép készítés gomb
gomb_kep = ttk.Button(root, text="Képernyőkép Készítés", command=keszit_kepernyokepet)
gomb_kep.pack()

# PDF generálás gomb
gomb_pdf = ttk.Button(root, text="PDF Generálás", command=generalt_pdf)
gomb_pdf.pack()

# Kilépés gomb
gomb_kilep = ttk.Button(root, text="Kilépés", command=root.destroy)
gomb_kilep.pack()

# A GUI futtatása
root.mainloop()

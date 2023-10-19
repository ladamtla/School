from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from PIL import Image
import os

# Mappa elérési útja, ahol a képek találhatók a "Képernyőképek" mappában
folder_path = "Képernyőképek/"

# PDF fájl neve, amibe az összefűzött képek kerülnek
pdf_file = "osszefuzott.pdf"

# Az összes .png kiterjesztésű fájl beolvasása a mappából
file_names = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]

# Ha nincs .png fájl a mappában
if not file_names:
    print("Nincs PNG fájl a megadott mappában.")
else:
    # Fájlnevek sorba rendezése
    file_names.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

    # PDF létrehozása és képek hozzáadása
    c = canvas.Canvas(pdf_file, pagesize=landscape(A4))

    for file_name in file_names:
        image = Image.open(os.path.join(folder_path, file_name))
        pdf_width, pdf_height = landscape(A4)

        # Kép méretének meghatározása a képarány megtartásával
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

        # Kép beillesztése a PDF-be eredeti képaránnyal
        c.drawImage(os.path.join(folder_path, file_name), x_offset, y_offset, width=new_width, height=new_height)

        # PDF oldal létrehozása a következő kép számára
        c.showPage()

    # PDF bezárása
    c.save()

    print(f'A(z) {pdf_file} fájl elkészült.')
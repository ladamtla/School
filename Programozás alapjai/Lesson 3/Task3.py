# Egy listában definiáljuk a napok neveit
napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

# Bekérünk egy sorszámot 1-7 ig
SorSzam = int(input("Adj meg egy számot 1-7-ig: "))

# A sorszám alapján lekérjük a listából a megfelelő napot
print(napok[SorSzam-1])
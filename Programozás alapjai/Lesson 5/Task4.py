# Definiáljuk a függvényt
def sumday(date):

    # A bemeneti sztringet szétmontjuk 3 válltozóra, majd számmá konvertáljuk
    y, m, d = date.split(sep=".")
    szum = 0
    y = int(y)
    m = int(m)
    d = int(d)
    i = 0
    szum = 0

    # Megvizsgáljuk, hoyg szökőév-e (Lesson3/Task5), majd különböző listákat definiálunk
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Az összeghez hozzáadjuk a hónapok napszámát, a jelenlegivel bezárólag
    for i in range(0, m):
        szum = szum + days[i]

    # Az összeghez hozzáadjuk a napok számát, amjd kivonjuk belőle az aktuális hónap napszámát (mivel az még nem telt el)
    szum = szum + d - days[m - 1]

    return szum

# Bekérjük a dátumot
date = input("Adja meg a dátumot az alábbi formátumban: (yyyy.mm.dd): ")

# Kiírjuk az eredményt
print(f"{date} az év {sumday(date)}. napja.")


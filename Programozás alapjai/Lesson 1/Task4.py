# Bekérünk egy dátumot: yyyy.mm.dd formátumban
date = input("Dátum: ")

# Szétbontjuk 3 válltozóba
y, m, d = date.split(sep=".")

# Definiákuk a válltozókat, egésszé konvertáljuk a dátum elemeit
szum = 0
i = 0
y = int(y)
m = int(m)
d = int(d)

# Szökőév vizsgálat
if y%4==0 and y%100 != 0 or y%400==0:
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Iterálunk 0-tól m-ig, hozzűadjuk az összeghez az adott hónap napszámát
for i in range(0, m):
    szum = szum + days[i]

# Hozzáadjuk az összeghez a maradék napok számát, majd kivonjuk az aktuális hónap napszámát (mivel az még nem telt el)
szum = szum + d - days[m-1]

# Kiírjuk az eredményt
print(f"{date} az év {szum}. napja.")
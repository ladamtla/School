# Bekérjük a másodpercek számát
mp = int(input("Add meg a másodpercek számát: "))

# Kiszámoljuk külön-külön a 3 értéket
min = mp // 60
mp = mp - min*60
hour = min // 60
min = min - hour*60

# Kiíratjuk a konzolra
print(f"{hour} óra {min} perc {mp} másodperc")
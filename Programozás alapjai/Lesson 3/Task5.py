# Bekérünk egy évszámot
y = int(input("Írj be egy évszámot: "))

# Megvizsgáljuk, hogy osztható-e 4-el, ha igen akkor megnézzük, hogy 100 al osztható-e, ha nem akkor szökőév.
# Valamint megnézzük, hogy 400-al ostható-e, ha igen akkor is szökőév.
# Kiírjuk az eredményt
if y%4==0 and y%100 != 0 or y%400==0:
    print(f"{y} év szököév")
else:
    print(f"{y} év nem szököév")
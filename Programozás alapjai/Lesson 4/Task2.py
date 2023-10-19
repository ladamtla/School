# Bekérünk egy kezdő és egy befejező évet
start = int(input("Add meg a kezdő évet: "))
stop = int(input("Add meg a befejező évet: "))

# Definiáljuk a kérdéses intervallumot
years = range(start,stop+1)
i = 0

# Egyesével végigmegyünk a lista elemein, megvigygáljuk, hogy szögőév-e, ha igen akkor hozzáadunk 1-et a segédválltozónkhoz (i)
for years in years:
    if years%4==0 and years%100 != 0 or years%400==0:
        print(f"{years} év szököév")
        i += 1
    else:
       print(f"{years} év nem szököév")

# Kiírjuk az eredményt
print(f"Összesen {i}db szökőév van {start} és {stop} között.")
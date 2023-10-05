
start = int(input("Add meg a kezdő évet: "))
stop = int(input("Add meg a befejező évet: "))

years = range(start,stop+1)
i = 0

for years in years:
    if years%4==0 and years%100 != 0 or years%400==0:
        print(f"{years} év szököév")
        i += 1
    else:
       print(f"{years} év nem szököév")

print(f"Összesen {i}db szökőév van a megadott tartományban.")
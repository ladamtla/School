y = int(input("Írj be egy évszámot: "))

if y%4==0 and y%100 != 0 or y%400==0:
    print(f"{y} év szököév")
else:
    print(f"{y} év nem szököév")
# Bekérünk egy számot
num = int(input("Adj meg egy számot: "))

# Mindaddig amíg a szám nagyobb 1-nél...
while num > 1:

    # ...ha páros elosztjuk hettővel
    if num % 2 == 0:
        num = num/2

    # ...ha páratlan a háromszorosához hozzáadunk 1-et
    else:
        num = num*3+1

    # Kiírjuk az eredményt
    print(int(num))
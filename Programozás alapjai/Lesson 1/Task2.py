# Definiáljuk az első 3 elemet
a = 0
b = 1
c = 1

# Kiírjuk az első elemet
print(a)

# Amíg c kisebb mint 1000, kiszámoljuk és kiírjuk a következő elemeket
while c < 1000:
    print(c)
    c = a + b
    a = b
    b = c
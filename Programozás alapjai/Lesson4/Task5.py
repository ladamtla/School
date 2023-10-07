
címletek = [200, 100, 50, 20, 10]


visszajáró_összeg = int(input("Kérem adja meg a visszajáró összeget: "))

címletek_száma = {}
for címlet in címletek:
    címletek_száma[címlet] = 0

for címlet in címletek:
    while visszajáró_összeg >= címlet:
        címletek_száma[címlet] += 1
        visszajáró_összeg -= címlet

print("Visszajáró összeg kifizetése:")
for címlet, darab in címletek_száma.items():
    if darab > 0:
        print(címlet, "címlet:", darab, "db")
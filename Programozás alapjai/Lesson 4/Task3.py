
num = 0
szum = 0
while True:
    num = input("Adj meg egy számot: ")
    if num == "":
        break
    else:
        num = int(num)
        szum = szum + num
print(f"A beírt számok összege: {szum}")
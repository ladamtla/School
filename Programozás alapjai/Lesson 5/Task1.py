# Definiáljuk a függvényt Lesson1/Task3 alapján
def collatz (num):
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        print(int(num))

# Ellenőrizzük a bemenetet, hogy 0-nál nagyobb legyen
while True:
    num = int(input("Number: "))
    if num > 0:
        break
    else:
        print("Value error")

# Meghívjuk a függvényt
collatz(num)
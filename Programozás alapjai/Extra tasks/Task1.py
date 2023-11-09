import random

counter = 1
ask = 1

while ask == 1:
    counter = 1
    RNum = random.randint(1, 100)
    while True:
        TNum = input("Melyik számra gondoltam?: ")
        TNum = int(TNum)
        if RNum == TNum:
            print(f"Eltaláltad {counter} lépésből!")
            break
        elif RNum > TNum:
            print("Nagyobb számra gondoltam!")
            counter += 1
            continue
        else:
            print("Kisebb számra fondoltam!")
            counter += 1
            continue
    while True:
        asker = input("Szeretnél tovább játszani? (y/n): ")
        if asker == "y" or "Y":
            ask = 1
            break
        elif asker == "n" or "N":
            ask = 0
            break
        else:
            continue
print("Vége a játéknak.")

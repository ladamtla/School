import random

ask = 1

while True:
    RNum = random.randint(1, 100)
    counter = 1
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

    asker = input("Szeretnél tovább számoldni? (y/n): ")
    if asker == "y":
        continue
    elif asker == "n":
        break



print("Vége a játéknak.")

pin = 123
i = 5

while i > -1:

    userPin = int(input("Írja be a PIN kódot: "))
    i -= 1
    if userPin == pin:
         print("Belépés engedélyezve")
         break
    elif i == 0:
        print("Belépés megtagadva, elfogtak a próbálkozások!")
        break
    else:
        print(f"Hibás PIN kód még {i} lehetőség van hátra")
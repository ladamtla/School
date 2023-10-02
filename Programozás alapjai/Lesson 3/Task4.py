napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

startday = int(input("Add meg az indulásod napját (Hétfő-Vasárnap) 1-7-ig: "))
time = int(input("Add meg a távollét időtartamát napok-ban: "))

finalday = (startday + time) % 7

print(f"A hazaérkezés napja: {napok[finalday-1]}")
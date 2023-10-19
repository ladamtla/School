# Egy listában definiáljuk a napok neveit
napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

# Bekérjük az indulási napot, és a távollét időtartamát nap(ok)-ban
startday = int(input("Add meg az indulásod napját (Hétfő-Vasárnap) 1-7-ig: "))
time = int(input("Add meg a távollét időtartamát napok-ban: "))

# Az érkezés napjának száma az idulási nap és az időtartam összegének a 7-el osztva kapott maradéka lesz
finalday = (startday + time) % 7

# Kiírjuk az eredményt (mivel 0-tól kezdődik a lista, így finalday-1)
print(f"A hazaérkezés napja: {napok[finalday-1]}")
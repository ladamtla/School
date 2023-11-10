import random

def wordGame (words):

    memory = []
    counter = 0
    rnum = random.randint(0, len(words)-1)
    word = words[rnum]
    base = ["_"] * len(word)
    print("Találd ki a szót:", " ".join(base))

    while "_" in base:
        index = 0
        tip = input("Van-e benne: ")
        counter +=1

        if tip in memory:
            print("Már kérdezted ")
            continue

        if tip in word:
            for letter in word:
                if letter == tip:
                    base[index] = tip
                index += 1
            print("Igen:", " ".join(base))
            memory.append(tip)
        else:
            print("Nincsen benne")
            memory.append(tip)
    print(f"Kitaláltad {counter} lépésből! Gratulálok!")


words = ["alma", "pisti", "józsi", "kerékpár", "anfiteátrum", "calypso", "ákos"]

wordGame(words)
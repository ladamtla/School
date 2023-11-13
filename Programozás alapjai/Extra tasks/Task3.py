
#semi-finished code, under writing...

import string

def textSeparator(text):
    clean = ""
    marks = string.punctuation
    for ch in text:
        if ch == marks or ch == ".":
            pass
        else:
            clean += ch
    clean = clean.lower()
    clean = clean.split(" ")

    return clean

def containE(words: list):
    """
    :param words: lista a szavakról
    :return: Összes szó száma, "e" betű tartalmazása százalékban
    """
    all = len(words)
    cone = 0
    for word in words:
        for ch in word:
            if ch == "e":
                cone += 1
                break
    estat = cone/all*100
    return all, estat

def searcher(words, sword):
    """
    megszámolja a szavak között a szót és egy egész számot ad vissza
    :param words: lista a szavakról
    :param word: keresett szó
    :return: előfordulás egész számban
    """
    counter = 0
    for word in words:
        if word == sword:
            counter += 1
    return counter

def wordFrequency(words: list):
    """
    :param words: lista a szavakról
    :return: egyes szavak előfordulását adja meg
    """
    uniquewords = []
    frequency = []
    for word in words:
        uniquewords.append(word)
        if word in uniquewords:
            pass
        else:
            fr = searcher(words, word)
            frequency.append(fr)

    for uword in uniquewords:
        print(f"'{uword}' szó eléfordul {frequency} alkalommal")





text = "A textémát egyetemes szövegegységnek kell tekintenünk, hiszen ha egy szövegben nincsen legalább egy textéma, akkor a nyelvi szintekre épülő nyelvtan logikájának megfelelően azt kell mondanunk, hogy valamely kisebb nyelvi elem alkalmilag tölti be a szöveg szerepét. A textéma a szöveghez viszonyítva hasonló szerepet játszik, mint a tőmorféma a szavak megformálásában vagy az alany állítmányi szószerkezet a mondat kialakításában. A tipikus szövegmű minimális formai feltétele tehát a bekezdésnyi méretű szövegegység jelenléte."
#text = "A textémát egyetemes szövegegységnek kell tekintenünk, hiszen ha egy szövegben nincsen legalább egy textéma"


words = textSeparator(text)
print(words)
print(containE(words))
wordFrequency(words)
import random

def calc_grade_rate(scores:list, grade:int):
    counter = 0
    if grade == 1:
        for s in scores:
            if s < 8:
                counter += 1
    elif grade == 2:
        for s in scores:
            if 8 <= s < 14:
                counter += 1
    elif grade == 3:
        for s in scores:
            if 14 <= s < 20:
                counter += 1
    elif grade == 4:
        for s in scores:
            if 20 <= s < 25:
                counter += 1
    elif grade == 5:
        for s in scores:
            if s >= 25:
                counter += 1

    return counter, counter/len(scores)*100

def in_grade5(scores: list, max) -> bool:
    found = False
    for s in scores:
        if s == max:
            found = True
            break
    return found



scores = []
for i in range(100):
    scores.append(random.randint(0, 30))


print(scores)
print(f"5-ösök száma és aránya: {calc_grade_rate(scores, 5)}")
print(f"Volt-e max pontos? {in_grade5(scores, 30)}")
print(f"Legmagasabb pontszám: {max(scores)}")
print(f"Legmagasabb pontszámú dolgozatok száma: {scores.count(max(scores))}")

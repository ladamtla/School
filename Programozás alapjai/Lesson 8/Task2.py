def bonus(lst: list):
    bonus = 0
    for i in lst:
        bonus = bonus + ((i // 4000)*10)
    return bonus

mylist = [22000, 13000, 10000, 2000, 5000]
print(bonus(mylist))
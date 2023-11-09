import random
def fill_list():
    lst = []
    for i in range(12):
        lst.append(random.uniform(17,22))
    return lst

def count_cold_days(lst: list) -> int:
    counter = 0
    for item in lst:
        if item < 20:
            counter += 1
    return counter


mylist = fill_list()
print(mylist)
print(f"Hideg volt a fürdéshez {count_cold_days(mylist)} nap")
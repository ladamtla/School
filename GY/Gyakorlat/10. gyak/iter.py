import itertools

l1 = [1, 2, 3, 4]

print(list(itertools.accumulate(l1)))

# loan 1000, 5% évente, 10 évig 100

print(list(
    itertools.accumulate(
        itertools.repeat(100, 10),
        lambda acc, init: (acc - init) * 1.05,
        initial=1000
    )
))

for i in zip(range(10), itertools.cycle(l1)):
    print(i)

l2 = [
    ("Hungary", "Miskolc"),
    ("Hungary", "Budapest"),
    ("Hungary", "Bag"),
    ("Germany", "Berlin"),
    ("Germany", "Munchen"),
    ("Great Britan", "Newcastle"),
    ("Great Britan", "London"),
]

cities = {}

for key, values in itertools.groupby(12, key=lambda x: x[0]):
    if cities.get(key) in None:
        cities[key] = []
    for city in values:
        cities[key].append(city[1])

print(cities)
def gAnd(a, b):
    return a and b
def gNand(a, b):
    return not a and b
def gOr(a, b):
    return a or b
def gNor(a, b):
    return not a or b
def Not(a):
    return not a

a = int(input("A: "))
b = int(input("B: "))
print(f"A és B: {gAnd(a, b)}")
print(f"A és B nem: {gNand(a, b)}")
print(f"A vagy B: {gOr(a, b)}")
print(f"A vagy B nem: {gNor(a, b)}")
print(f"A nem: {Not(a)}")
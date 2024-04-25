from dataclasses import dataclass

l = [1, 2, 3, 4, 7, 12, 5]
print(max(l))

@dataclass
class Employee:
    name: str
    age: int

employees = [
    Employee("John Doe", 24),
    Employee("Ben Dover", 56),
    Employee("John Travolta", 71)
]

def oldest_employee(emps: list[Employee]):
    return max(emps, key=lambda emp: emp.age)

print(max(employees, key=lambda emp: emp.age))
print(min(employees, key=lambda emp: emp.age))

print(sorted(employees, key=lambda emp: emp.age))

print(list(filter(lambda emp: emp.age > 30, employees)))

employees.append(None)
print(employees)
print(list(filter(None, employees)))
print(list(filter(None, [0, 1, 1, 0, 0, 3])))

print(map(lambda x: x ** x, [1, 4, 5, 1]))
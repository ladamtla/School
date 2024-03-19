import random

def get_yearly_income(years: int) -> list[int]:
    income = []
    for _ in range(years):
        income.append(random.randint(15000,85000))
    return income

def print_net_income(yearly_income: list[int]):
    print("Net yearly income: ")
    print("Year\tIncome($)")
    for index, income in enumerate(yearly_income):
        print(f"|{index + 1:<10} |{income:>10,}|")


income = get_yearly_income(10)
print_net_income(income)
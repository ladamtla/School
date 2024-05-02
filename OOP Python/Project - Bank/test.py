from customer import Customer
from bankaccount import BankAccount

ba = BankAccount(111111111111111111111111, 500, [], [], 1)
customer = Customer("Péter", "+362055454458", "d@gg.ji", "Kács", "llh", "123", 1, 1, ba)

print(customer)
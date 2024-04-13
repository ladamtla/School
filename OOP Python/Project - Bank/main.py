from admin import Admin
from employee import Employee
from customer import Customer

admin1 = Admin("Ádám","+36204472104", "ladam050406@gmail.com", "Mnyarad", "ladamtla", "AdamT", 789)
cust1 = Customer("Ádám","+36204472104", "ladam050406@gmail.com", "Mnyarad", "ladamtla", "AdamT", 215)
emp1 = Employee("Ádám","+36204472104", "ladam050406@gmail.com", "Mnyarad", "ladamtla", "AdamT", 7899)
print(admin1)
print(cust1)
print(emp1)
Admin.data_updater(admin1)
print(admin1)

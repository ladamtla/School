from datetime import datetime
import random

expdate = datetime.now()
expdate = str(expdate)
year = expdate[2:4]
month = expdate[5:7]
year = int(year)
expdate = year + random.randint(3,5)
expdate = str(expdate)
expdate = month + "/" + expdate

print(expdate)
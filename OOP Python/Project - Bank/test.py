from datetime import datetime

expdate = datetime.now()
expdate = str(expdate)
year = expdate[2:4]
month = expdate[5:7]
year = int(year)
expdate = year + 3
expdate = str(year)
expdate = month + "/" + expdate

print(expdate)
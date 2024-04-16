class Transactions:
    def __init__(self, tranID: str, date: str, time: str, amount: str, type: str):
        self.tranID = tranID
        self.date = date
        self.time = time
        self.amount = amount
        self.type = type

    def __str__(self):
        return f"ID: {self.tranID}\nDátum: {self.date}\nIdő: {self.time}\nÖsszeg: {self.amount}\nTípus: {self.type}"
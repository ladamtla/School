class BankAccount:
    def __init__(self, accountNum: str, balance: int, bankCards: list, transactions: list, baID: int):
        self.accountnum = accountNum
        self.balance = balance
        self.bankCards = bankCards
        self.transactions = transactions
        self.baiID = baID


    def __str__(self):
        return f"Számlaszám: {self.accountnum}\nEgyenleg: {self.balance}\nBankkártyák: {self.bankCards}\nTrancakciók: {self.transactions}\nTrancakciók: {self.baiID}"
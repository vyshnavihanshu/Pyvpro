class Bank:
    Bank_name = "CV Bank"
    def __init__(self,name,  balance):
        self.holder = name
        self.balance= balance
    @classmethod
    def change_bname(cls,newname):
        cls.Bank_name = newname
    def deposite(self,amount):
        self.balance+=amount
    @staticmethod
    def validate(amount):
        return amount > 0
b1 = Bank("vyshu",10000000)
b1.change_bname("cvcorp")
Bank.change_bname("cvcorp")
b1.deposite(10000000)

print(b1.validate(10000000))
print(Bank.validate(b1.balance))
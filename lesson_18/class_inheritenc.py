# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero.
class BankAccount:
    def __init__(self, accaunt_number, balance):
        self.number = accaunt_number
        self.balance = balance
    def deposit(self,avelacnel):
        if avelacnel > 0:
            self.balance = self.balance + avelacnel
        else:
            return (f"{self.number} chem karox avelacnel ")
    def withdraw(self, gumar):
        if self.balance >= gumar:
            self.balance = self.balance - gumar
        else:
            return f"{self.number} anbavarar mijocner"
    def Balance(self):
        return self.Balance()
class SavingsAccount(BankAccount):
    def __init__(self, accaunt_number, balance, interest_rate):
        super().__init__(accaunt_number, balance)
        self.rate = interest_rate
    def avand (self, amount):
        super().deposit(amount)
        self.balance += self.balance * self.rate
class CheckingAccount(BankAccount):
    def __init__(self, accaunt_number, balance, overdraft_fee):
        super().__init__(accaunt_number, balance)
        self.overdraft = overdraft_fee
    def withdraw(self, gumar):
        if self.balance >= gumar:
            super().withdraw(gumar)
        else:
            self.balance -= self.overdraft
            print(f"you don't have many overdraft pay ")

accaunt1 = SavingsAccount("454545456",500, 0.05)
accaunt1.avand(500)
accaunt2 = CheckingAccount("454465", 150, 35)
accaunt2.withdraw(210)
print(accaunt2.balance)
print(accaunt1.balance)


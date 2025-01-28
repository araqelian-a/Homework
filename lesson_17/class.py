# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information.
class BankAccount:
    def __init__(self, accaunt_holder, balance):
        self.name = accaunt_holder
        self.balance = balance
    def deposit(self,avelacnel):
        if avelacnel > 0:
            self.balance = self.balance + avelacnel
            print(f"{self.name} balance avelacav {avelacnel} nor balance  = {self.balance}")
        else:
            print(f"{self.name} chem karox avelacnel ")
    def withdraw(self, gumar):
        if self.balance >= gumar:
            self.balance = self.balance - gumar
            print(f"{self.name} kanxikacum = {gumar}")
        else:
            print(f"{self.name} anbavarar mijocner")
    def Balance(self):
        print(f"{self.name} balance = {self.balance}")
accaunt_1 = BankAccount("Artavazd",1000)
accaunt_1.deposit(500)
accaunt_1.withdraw(200)
accaunt_1.Balance()


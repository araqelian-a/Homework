# Create a class called BankAccount to represent a basic bank account. The class should
# have the following attributes:
# 1. owner: The name of the account owner.
# 2. balance: The current balance of the account.
# Implement the following methods:
# 1. __init__(self, owner, balance): Initializes the BankAccount object with the
# owner's name and initial balance. Ensure that the balance is a non-negative
# integer.
# 2. get_balance(self): Returns the current balance of the account.
# 3. deposit(self, amount): Adds the specified amount to the account balance.
# Ensure that the amount is a positive integer.
# 4. withdraw(self, amount): Subtracts the specified amount from the account
# balance. Ensure that the amount is a positive integer and does not exceed the
# current balance.
# Additionally, use @property and @attribute.setter to encapsulate the balance
# attribute and enforce validation rules.
class BankAccount:
    def __init__(self, accaunt_holder, balance):
        self.name = accaunt_holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    def deposit(self, num):
        if num > 0:
            self.__balance = self.balance + num
            print(f"{self.name} balance uptade {num} new balance = {self.__balance}")
        else:
            print(f"{self.name} i can't add ")
    def withdraw(self, num, overdraft_fee):
        if self.__balance >= num:
            self.__balance = self.__balance - num
            print(f"{self.name} decrease = {num}")
        else:
            self.__balance -= num + overdraft_fee
    @balance.setter
    def balance(self):
        return self.balance


accaunt_1 = BankAccount("Artavazd", 1000)
print(accaunt_1.balance)
accaunt_1.deposit(0)
accaunt_1.withdraw(1100, 25)
print(accaunt_1.balance)


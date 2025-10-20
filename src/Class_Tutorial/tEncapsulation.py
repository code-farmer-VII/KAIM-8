class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder   # public attribute
        self.__balance = balance               # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance  # controlled access

# Example usage
account = BankAccount("Temesgen", 1000)
account.deposit(500)
print(account.get_balance())  


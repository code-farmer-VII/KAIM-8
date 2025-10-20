class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Deposit amount must be postive.")
    def wisdrow(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")
    def getBalance(self):
        print(f" {self.account_holder}'s Current balance is {self.__balance}")
account = BankAccount("Temesgen", 1000)

account.getBalance()
account.deposit(500)
account.getBalance()

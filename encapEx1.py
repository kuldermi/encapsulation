class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def check_balance(self):
        print(f"This is the balance of {self.owner}: {self.__balance}")


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            return "Incorrect amount"


myAccount = BankAccount("Dermi", 100)
myAccount.check_balance()                
myAccount.deposit(200)
myAccount.check_balance()

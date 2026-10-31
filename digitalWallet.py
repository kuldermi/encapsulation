class DigitalWallet:
    def __init__(self):
        # self.__balance = balance
        self.__balance = 0

   
    def add_money(self, inputAmount):
        self.inputAmount = inputAmount
        self.__balance += inputAmount

        if self.inputAmount > 0:
            print(f"Your current balance is {self.__balance} .  ")
        else: 
            print(" Enter amount greater than 0. ")        

    def deduct_fare(self, fare):
        self.fare = fare
        if fare > self.__balance:
            print(f"Insufficient balance, please recharge. ")  
        else:
            self.__balance -= fare
            print(f"Your wallet balance is after deduction {self.__balance}")            
    def get_balance(self):
        print(f"This is the curernt balance {self.__balance}")



myWallet = DigitalWallet()

# myWallet.__balance = -20
# print(myWallet.__balance)
myWallet.add_money(104)
myWallet.deduct_fare(120)
myWallet.get_balance()
  

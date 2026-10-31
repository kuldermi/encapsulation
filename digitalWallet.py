class DigitalWallet:
    def __init__(self):
        # self.__balance = balance
        self.__balance = 0

    def add_money(self, inputAmount):
        self.inputAmount = inputAmount
        if self.inputAmount > 0:
            print(f"Your current balance is {self.__balance + inputAmount} .  ")
        else: 
            print(" Enter amount greater than 0. ")        

    def deduct_fare(self, fare):
        self.fare = fare
        if fare > self.__balance:
            print(f"Insufficient balance, please recharge. ")          

myWallet = DigitalWallet()
myWallet.add_money(103)
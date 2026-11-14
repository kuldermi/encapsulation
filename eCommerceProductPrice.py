class Product:
    def __init__(self, price):
        self.__price = 0
        self.price = price    

    @property    
    def price(self):
        return self.__price
    @price.setter    
    def price(self, inputPrice):
        if inputPrice <= 0:
            print(f"Enter a positive value , price can't be negative")
        else:
            self.__price = inputPrice   
            print(f"Your current product price is {self.__price}")      

myProduct = Product(30)
myProduct.price = 70


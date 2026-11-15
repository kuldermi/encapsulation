class Person:
    def __init__(self):
        self.__age = 0
    @property
    def age(self):
        return self.__age
    @age.setter    
    def age(self, inputAge):
        if inputAge <= 0 or inputAge > 120:
            print(f"Enter age greater than 0 but less than 120 ")
        else:
            self.__age = inputAge  
            print(f"Your age is {self.__age}")  

myAge = Person()
myAge.age = 130
class CoffeeMachine:
    def __init__(self):
        self.__waterLevel = 100
        self.__beans = 10
      
# water level and beans are private so that it can't be accessed from outside
# make coffee method will check the water level and beans
# Coffee beans  and water will be full at first
# customer will take the first coffee
# coffee beans and water level will go down by coffee amount
# Next time it will check the waterLEvel and coffee beans
    @property
    def waterLevel(self):
        return self.__waterLevel
    @property    
    def beans(self):
        return self.__beans



    def make_coffee(self):
        if self.__waterLevel <= 0:
            print("insufficient water. filling it up , wait")
            self.__waterLevel = 100
            print(f"Your waterlevel is filled now you have {self.__waterLevel} ml. ")
        if self.__beans <=0:
            print("insufficient beans. filling it up , wait. ")
            self.__beans = 10
                
        self.__waterLevel -= 50
        self.__beans -=5
        print(f"waterLevel is {self.__waterLevel}")
        print(f"Beans are {self.__beans}")
        print("Here is your coffee. enjoy.")
myCoffee = CoffeeMachine()
myCoffee.make_coffee()
myCoffee.make_coffee()
myCoffee.make_coffee()
class Car:
    def __init__(self):
        self.__speed = 0

    @property
    def speed(self):
        return self.__speed


    def accelerate(self, increaseSpeed):
        if 0 < increaseSpeed:
            self.__speed += increaseSpeed
            print(f"Your vehicle is accelerating with speed {self.__speed} km /h ")
            
    def brake(self, decreaseSpeed):
        if decreaseSpeed > 0:
            self.__speed -= decreaseSpeed
            if self.__speed < 0:
                self.__speed = 0
                print(f"Your vehicle is moving at {self.__speed} km/h")

        
                      


myCar = Car()
myCar.accelerate(40)
myCar.brake(50)


#print(f"My final speed {myCar.speed} km/h")
class SmartPhone:

    def __init__(self, battery_level):
        self.__battery_level = battery_level
        print(f"This is the current battery level : {self.__battery_level}")
        # return f"This is the battery level {self.__battery_level}"

    def use_phone(self, minutes):
        self.minutes = minutes
        self.__battery_level -= minutes
        if self.__battery_level < 180:
            print(f"This is less than 180 , current level {self.__battery_level}")
        elif self.__battery_level <= 0:
            print("Plug into charger, your phone might be dead. ")

        # else self.__battery_level <= 0:
        #     print("Plug into charger, otherwise your phone might be dead.")


myPhone = SmartPhone(100)
myPhone.use_phone(10)





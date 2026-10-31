class Thermostat:
    def __init__(self):
        self.__temparature = 25

    def get_temparature(self):
        print(f"This is the current temparature. {self.__temparature} ")

    def set_temparature(self, temparature):
        self.__temparature = temparature
        print(self.__temparature)
        if int(self.__temparature) >= 30 or int(self.__temparature) <=18:
            print(f"The temparature is not in safe zone. ")    
        else:
            print("The temparature is in safe zone.")

myThermostat = Thermostat()

myThermostat.get_temparature()
myThermostat.set_temparature(87)
myThermostat.get_temparature()
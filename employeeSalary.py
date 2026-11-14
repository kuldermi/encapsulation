class Employee:
    def __init__(self):
        self.__salary = 100 

    @property
    def salary(self):
        return self.__salary
    
    def give_raise(self, hikePercentage):
        if hikePercentage > 0:
            self.__salary += self.__salary * (hikePercentage / 100 )
        elif hikePercentage <= 0:
            self.__salary += self.__salary * (hikePercentage/100)
            print(f"Your updated salary is {self.__salary}")


myEmp = Employee()
myEmp.give_raise(-10)
myEmp.__salary = -10
print(f"My salary is {myEmp.salary}")
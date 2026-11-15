class Member:
    def __init__(self, memberName):
        self.__status = "expired"
        self.memberName = memberName
    @property    
    def status(self):
        return self.__status
    @status.setter
    def status(self, feePaid):
        if feePaid == "y":
            self.__status = "active"   
            print(f"The membership is active for {self.memberName}")
        else:
            self.__status = "expired"
            print(f"The memebership of this person {self.memberName} is expired. ")    

myGym = Member("Abc")

myGym.status = "n"
myGym.status = 'y'

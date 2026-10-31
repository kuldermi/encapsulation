class User:
    def __init__(self, user, password):
        self.user = user
        self.__password = password
    def set_password(self):
        if len(self.__password) <= 6:
            print("Password is too short!. ")
    def check_password(self, input_password):
        if self.__password == input_password:
            print("Logged in successfully. ")
        else:
            print("You have enterend incorrect password. ")

myUser = User("Dermi", "Pass")
myUser.set_password()      
myUser.check_password("Password1")                    

class Password:
    def __init__(self, password):
        self.__password = ""
        self.password = password
    @property
    def password(self):
        return  "*" * len(self.__password)

    @password.setter
    def password(self, inputPassword):
        if len(inputPassword) < 8:
            print(f"Enter more than 8 characters to make password strong.")
        else:
            self.__password = inputPassword 
            print(f"Your password is set.")      


myPassword = Password("123")
#myPassword.password = "123456789"            

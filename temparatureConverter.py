class Celsisus:
    def __inti__(self):
        self.__temparature = 0

    def temrature_converter(self, inputTemparature):
        if inputTemparature < -273.15:
            print(f"Enter correct input. ")
        else:    
            self.tempFarenheit = float((inputTemparature * 9 /5 )+ 32)
            if self.tempFarenheit < -459.4:
                self.__temparature = 0
                print(f"The temrature can't move beyond -459.4 f, current temparature {self.__temparature}")
            else:
                self.__temparature = self.tempFarenheit
                print(f"The temparature in farenheit {self.__temparature}")    

myTemp = Celsisus()
myTemp.temrature_converter(-274)
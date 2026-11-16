class Theater:
    def __init__(self):
        self.__availableSeats = 100
    @property
    def availableSeats(self):
        return self.__availableSeats    
    def bookTicket(self, inputTickets):
        if inputTickets <= 0:
            print("Tickets can't be less than or equal to 0.")   
        elif inputTickets > self.__availableSeats:
            print("Tickets are unavailable. ")     
        else:
            self.__availableSeats -= inputTickets
            print(f"Here are your {inputTickets} tickets , enjoy.")
            print(self.__availableSeats)
            

myTickets =Theater()
myTickets.bookTicket(100)
myTickets.bookTicket(10) 
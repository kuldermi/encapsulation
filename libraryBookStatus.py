class Book:
    def __init__(self, book_name):
        self.book_name = book_name
        self.__is_borrowed = False
        
    @property
    def borrow(self):
        return self.__is_borrowed
        
    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"The book {self.book_name} has been borrowed by you.")
        else:
            print("The book is borrowed by someone else.")    
    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            print(f"Thanks for returning the book {self.book_name}")
        else:
            print(f"The {self.book_name} was not borrowed , so it cannnot be returned. ")            

myBook = Book("The intelligent Investor")
myBook.borrow()
myBook.borrow()

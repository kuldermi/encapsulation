class Book:

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return f"This is the title of the book : {self.__title}"

    def get_author(self):
        return f"This is the author name : {self.__author}"

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author    


myBook = Book("Intelligent Investor", "Ben Graham")

# myBook.get_author()

myBook.set_author("Dale Carnigie")
myBook.set_title("Communication course.")
print(myBook.get_title())
print(myBook.get_author())

try:
    myBook.__title = "Harry Potter"
    print(f"After change,  {myBook.get_title()}")

except Exception as e:
    print("This is the error message", e)

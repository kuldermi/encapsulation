class Student:
    def __init__(self):
        #self.__marks = marks
        self.__marks = 0
    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def update_mark(self, inputMarks):
        if 0 < inputMarks <= 100:
            self.__marks = inputMarks
            print(f"Your updated marks is: {self.__marks} ")
        else:
            print(f"Enter the mark between 0 and 100.")

myStudent = Student()
myStudent.update_mark = 90
myStudent.update_mark = -20
myStudent.__marks = 12
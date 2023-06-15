# Inheritance ----> Inherits Property from another class

# 1. Single Inheritance

class Father:

    def __init__(self):    # Constructor
        self.car = "Alto"
        self.home = "Ambika"
        print("class Father ---> variables Created ")

    def show_properties(self):
        print(self.car, self.home)

    @staticmethod   # Utility work
    def declaration():
        print("Hello This is static Method under Father class.")

class Mother:
    def hello(self):
        pass

# class Henish : public Father
class Henish(Father, Mother):

    def __init__(self):
        super().__init__()
        self.laptop = "dell"
        self.mobile = "htc"
        print("class Henish ---> variables Created ")

    def show_hproperty(self):
        print(self.laptop, self.mobile)


h1 = Henish()

h1.show_hproperty()  # dell htc
h1.declaration()   # Hello This is static Method under Father class.
h1.show_properties()   # Alto Ambika
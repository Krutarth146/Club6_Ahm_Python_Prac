# # Inheritance ----> Inherits Property from another class

# # 1. Single Inheritance

# class Father:

#     def __init__(self):    # Constructor
#         self.car = "Alto"
#         self.home = "Ambika"
#         print("class Father ---> variables Created ")

#     def show_properties(self):
#         print(self.car, self.home)

#     @staticmethod   # Utility work
#     def declaration():
#         print("Hello This is static Method under Father class.")

# class Mother:
#     def hello(self):
#         pass

# # class Henish : public Father
# class Henish(Father, Mother):

#     def __init__(self):
#         super().__init__()
#         self.laptop = "dell"
#         self.mobile = "htc"
#         print("class Henish ---> variables Created ")

#     def show_hproperty(self):
#         print(self.laptop, self.mobile)


# h1 = Henish()

# h1.show_hproperty()  # dell htc
# h1.declaration()   # Hello This is static Method under Father class.
# h1.show_properties()   # Alto Ambika


# ----------------------------------------------
# PolyMorphism


class Employee:
    def __init__(self,need):
        self.time = need


    def print_time(self):
        print("Method called",self,self.time)  # 
# Method called <__main__.Employee object at 0x0000014CD0C16500> 1500


class Customer(Employee):
    def __init__(self, need):
        super().__init__(need)
        self.maal = need
        print("Constructor: mal value",self.maal)



    def mult(self, num1 , num2):
        print(num1 * num2)

    def mult(self, num1,num2,num3):
        print(num1 * num2 * num3)

    def mult(self):
        print("Mult Method")

    # def print_time(self):
    #     print("Time is Precius")

    


# e1 = Employee(900)
# e1.print_time()

# aagam = Customer(600, 800)   # 800
# aagam.print_time()    # Time is Precius


# emp = [Employee(1500), Customer(901)]
# print()
# print()
# for e in emp:
#     # print(e)  # <__main__.Employee object at 0x0000026FC62FB6A0>, <__main__.Customer object at 0x0000026FC62FB700>
#     e.print_time()


Maahir = Customer(500)
Maahir.mult()

# Polymorphism

# Poly - Many
# Morph - FOrms

#   right ----> right - wrong, right - left


# len(), sum(), min()   # Polymorphism --->  Methods
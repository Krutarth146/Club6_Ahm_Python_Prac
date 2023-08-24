# print(89/0)  # DIvisionbyzeroError

x = 90
y = 'ABC'

# print(x+y)   # TypeError


# x = int(input())  # ValueError

# x = open("Hello.txt",'r')  # FileNotFoundError

# IOError
# AttributeError
# Import Error
# name Error
# syntax Error

# import tensorflow  # : No module named 'tensorflow'

# numpy.random()   # NameError

# import maahir  # ModuleNotFoundError: No module named 'maahir'

# while
#     paasss
#synatx


# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 + num2)

# except NameError:
#     print("NameError Occured")
# except ArithmeticError:
#     print("ArithmeticError Occured")
# # except ValueError:
# #     print("valueError Occured")
# # except:
# #     print("Error Generated")
# # except Exception as e:
# #     print("Error Generated",e)

# else:
#     print("This is Else Block")

# finally:
#     print('This is Finally which is Always Executed')

# print('This is Finally which is Always Executed')


# Built in Exceptions


def factorial(num):
    try:
        mul = 1
        for i in range(1,num+1):
            yield i
    except GeneratorExit:
        print("Existing Early")

# for j in factorial(5):
#     print(j)   

f1 = factorial(5)

print(f1.__next__())   # 1
print(f1.__next__())   # 2
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())


def create_file():
    try:
        with open ("first1.txt",'r') as f:
            f.write("Hello")
    except IOError:
        print("Wrong Operation")

create_file()


# User Defined Exception

# class Error(Exception):
#     """Base class for other Exception"""
#     pass


class Maahir(Exception):
    pass

try:
    num = int(input())
    if num == 0:
        raise Maahir
    print(20/num)
    

except Maahir:
    print("Very Wrong Dicision")


# print(Error.__doc__)   # Base class for other Exception
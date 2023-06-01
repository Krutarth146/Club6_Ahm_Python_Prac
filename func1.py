# UDF

# 1. No Return type and No args 
# 2. No return Type and With args
# 3. With Return type and Without args
# 4. With retrun type and with args


# 1. No Return type and No args 
def jayraj():
    print("Hello I am Jayraj")

# 2. with return Type and Without args

def henish():
    x,y,z = 30,10,80
    return x+y, y-z

print(henish())  # (40, -70)

# 3. Without Return type and With args

def authentication(email,password):
    if password.isalpha():
        print("Password Invalid")
    elif password.isnumeric():
        print("Password Invalid")
    elif len(password) > 7:
        print("Valid Password")
    else:
        print("Invalid Password")
    

    if email.strip().endswith("@gmail.com"):
        print("Email Valid")
    else:
        print("EMail Invalid")


authentication('jayraj12@gmail.com', "vsdsdvsdv12")

str1 = "    sdvncsdvsd        "

print(str1.strip())


# 4. with return type and with args.

def royal(num):
    mul = 1
    for i in range(1,num+1):
        mul *= i
    return mul

print(royal(5))  

def series(num):
    for i in range(num):
        yield i
    

# print(series(5))  # <generator object series at 0x0000024617619A10>

for i in series(5):
    print(i)

# 4 types

# oye balle balle oye  --> Que
# OyE BallE BallE OyE  --> Ans

# upper(), split(), title(), Indexing


str1 = "oye balle balle oye"
str1 = str1.title()
list1 = str1.split()
print(list1)

list2 = []
for i in list1:
    temp = i[::-1]
    temp = temp.replace("e",'E',1)
    temp = temp[::-1]
    list2.append(temp)

print(list2)

str2 = ' '.join(list2)
print(str2)


def mul(x,y,z=1):
    return x*y*z

print(mul(10,20,90))  # 18000   # Default Function


# Args ----------------------

def div(x,y,z,*jay,b=0):
    for i in jay:
        print(i)
    print(jay)

div(10,20,30,"Jay",56,89)  # (10, 20, 30, 'Jay')


def kru(*henish,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
    print()
    print()
    print(henish)   # (30, 40, 50, 60)

kru(30,40,50,60,name='Krutarth', roll = 900, address = 'Ahm')  # {'name': 'Krutarth', 'roll': 900, 'address': 'Ahm'}


# from bidict import bidict
def car_details(**creta):
    print(type(creta))  # <class 'dict'>

    # creta2 = bidict.inverse

    print(creta['price'])
    print(creta.get('year'))
    # print(creta.get('Creta1'))

car_details(name="Creta1", model = 'xx', year = 2022, price = 700)

# Recursion, lambda, Map, reduce, filter

# Task:

'''
take two numbers from user in getdata function , 
this function will return odd number from both if both are odd 
then return max from it. 

now use this number to check its prime or not using 
prime(num) function. 
prime function return 1 if num is prime and -1 if not prime 

print 1 or -1 in the output screen

17,20 
1 

30,9
-1 

15,19 
1 

20,40
-1
'''

# Check whether string is Palindrome or not??    str1 = "Nayan" -> Palindrome


# Decorators --->

# decorator is First Class Object

# Function have Inner Functions

# It takes function as a Argument

def fun1():
    print("Inside fun1")

def fun2(f):
    print("Inside fun2")
    f()


# fun2(fun1)
# Inside fun2
# Inside fun1
print()
f = fun1
print(type(f))   # <class 'function'>

f()   # Inside fun1
print()
fun2(f)

# Inside fun2
# Inside fun1


# --------------------------------------------

def fun5(f):
    def innerfun():
        print("Henish")
        f()

    return innerfun

@fun5   # Decorator
def fun6():
    print("Mahhir")


# fun = fun5(fun6)
fun6()

# Henish
# Mahhir



str1 = "python"
str1 = "aeiou"

for i in str1.lower():
    if i == 'o' or i == 'u' or i == 'a' or i == 'e' or i == 'i':
        str1 = str1.replace(i, chr(ord(i) - 30))

print(str1)
print("%c" %65)  # A


l1 = [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]

dict1 = {}
counter = 0
c = 0
for list1 in l1:
    for word in list1:
        for char in word:
            counter+=1
        c= counter
    dict1[counter] = list1
    counter = 0

ans = min(dict1)
print(dict1[ans])


# https://leetcode.com/problems/contains-duplicate/

# https://leetcode.com/problems/maximum-subarray/

# https://www.geeksforgeeks.org/chocolate-distribution-problem/

print(90 ^ 89)  # 3
print(90 | 9001)  # 3
print(90 & 9001)  # 3

print(bin(90))  # 0b1011010
print(bin(89))  # 0b1011001
# print(hex(90))  # 0b5a
# print(oct(90))  # 0o132
# print(0b010101)  # 21


# 1011010
# 1011001
# -------
# # 0000011
print(0b0000011)  # 3

l1 = [("ca",('cat', 'car', 'fear', 'center'))]

print(len(l1))  # 1

tup1 = l1[0][1]

for i in tup1:
    if l1[0][0] in i:
        print(i)
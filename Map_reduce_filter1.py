list1 = [10,20,30,40,50,60]

ans = []
for i in list1:
    ans.append(i**2)

print(ans)   # [100, 400, 900, 1600, 2500, 3600]

# Powerful Function

# map()


# lambda  --> Anounomus Function

ele = 90

def square(ele):
    return ele**2

print(square(ele))  # 8100

func = lambda ele,num2,num3 : ele * num2 * num3

print(func(60,40,32))   # 76800

cube = lambda x : x**3
print(type(cube))  # <class 'function'>
print(cube(11))  # 1331

list1 = [10,20,30,40,50,60]
res = list(map(lambda x : x**3, list1))
print(type(res))   # map
print(res)   # [1000, 8000, 27000, 64000, 125000, 216000]


# Quadratic Function 
# a * x ** 2 + b * x + c

def Quadratic_fun(a,b,c):
    return lambda x : a * x ** 2 + b * x + c

royal = Quadratic_fun(10,20,30)

print(royal(5))   # 380

list2 = [20,30,40,50,60]

# sum = 0
# for u in list2:
    # sum += u


# Reduce
from functools import reduce

res2 = reduce(lambda x, y : x + y, list2)

print(res2)   # 200

from itertools import accumulate

list2 = [20,30,40,50,60]
res3 = tuple(accumulate(list2, lambda x, y : x + y))
print(res3)  # (20, 50, 90, 140, 200)


# Filter

fil1 = list(filter(lambda f : f > 40, list2))  # [50, 60]
# fil1 = list(map(lambda f : f > 40, list2))   # [False, False, False, True, True]
print(fil1)  # [50, 60]

avg = list(filter(lambda c : (sum(list2) // len(list2)) < c, list2))

print(avg)  # [50,60]

import statistics

# avg1 = statistics.mean(list2)
avg = list(filter(lambda c : statistics.mean(list2) >= c, list2))
print(avg)  # [20, 30, 40]


# Recursion  ---> When FUnction calls Itself then it is called as Recursion

def fibonnacci(step):
    n1,n2 = 0 , 1

    print(n1,n2,end=' ')

    for i in range(step-2):
        n3 = n1 + n2
        print(n3,end=' ')
        n1 = n2
        n2 = n3

fibonnacci(5)

print()
print()

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonnaccci_rec(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonnaccci_rec(num-1) + fibonnaccci_rec(num-2)

# print(fibonnaccci_rec(5))   # 5

for i in range(50):
    print(fibonnaccci_rec(i),end=' ')  # 0
 

# Map, reduce, filter, recursion ---> 5 Programs
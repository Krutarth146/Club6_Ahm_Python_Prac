def sum():
    for i in range(-2,-6,-2):
        yield i
    print("Executed")


# print(sum())

for j in sum():
    print(j)

# Lambda function



# if num % 5 == 0:
#     print("num is d by 5")
# else:
#     print("N D")

# "nu is d by 5" if num % 5 == 0 else "N D"

dby5 = lambda num : "num is d by 5" if num % 5 == 0 else "N D"

print(dby5(41))

a = 90
b = 80
c = 70 

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

x = a if a > b and a > c else c if b < c else b
print(x)

cube = lambda a : a*a*a

print(cube(2))


# ----------------------

list1 = ["1", "2", "3", "4", "-1"]
list1 = sorted(list1,key=lambda x : int(x))
print(list1)


# Map ->  [1,2,3,4,5] -> [1,4,9,16,25]
list2 = [1,2,3,4,5,90,8,67,7]
result = list(map(lambda x : x * x, list2))  # [1, 4, 9, 16, 25]
print(result)

# filter ->   [1,3,6,8,10] -> [6,8,10]
gby5 = filter(lambda x : x >= 5,list2)
print(list(gby5))  # [5, 90, 8, 67, 7]
    
# print(lambda x : x >= 5,list2)

# Reduce ->   [1,2,3,4,5]  -> 120
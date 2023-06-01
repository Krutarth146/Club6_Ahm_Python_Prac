str = "Krutarth"
print("My name is",str)

name = "Helly"
Mode = 'Good'
Number = 123


print("My name is",name)
print("{} is {} Girl.".format(name, Mode))  # Helly is Good Girl.
print("{1} is {2} Girl.{0}".format( Number, name, Mode))  # Helly is Good Girl.123
print("{pro} is Good {gender}.{num}".format( num = 123, pro = "Henil", gender = "Boy"))  # Henil is Good Boy.123

print(f"3 * 2 is {3*2}")   # 3 + 2 is 6   # fstring




#--------------------------------------------------------------
list1 = ['Apple', 'mango', 'cherry', 'pineple']

# fruit = input()  # mango
   
# for _ in list1:    # Like linear search
#     # print(_)           
#     if _ == fruit:   # Apple == mango
#         print(f"{fruit} is available")
#         break
    

# Membership Operator - > in , not in

# if fruit in list1:
#     print(f"{fruit} is available")
# else:
#     pass


#----------------- List Comprehension -------------------------------

lst3 = [9,2,1,3,5,6,7]
ans = []

for rohan in lst3:  # 34
    ans.append(rohan * rohan * rohan)   # cube store in ans (list)
print(ans)

result = [_*_*_ for _ in lst3]
print(result)  # [729, 8, 1, 27, 125, 216, 343]
print(type(result))  # <class 'list'>



lst3 = [9,2,1,3,5,6,7]
odd = [i for i in lst3 if i % 2 != 0]
print(odd)   # [9, 1, 3, 5, 7]


# [(1,1) , (2,8), (3,27), (4,64) , (5,125)]

cube = list((i,i*i*i) for i in range(1,6))
print(cube)   # [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]


lst6 = [3,6,1,8,9]
lst9 = [6,5,3,2,8]
list11 = []
# [(3,6), (3,5), (3,3), (3,2)...............]

for i in lst6:   # 3 6
    for arin in lst9:   # 6 5 3 2 8   6,5,3,2,8
        list11.append((i,arin)) 

print(list11)    # [(3, 6), (3, 5), (3, 3), (3, 2), (3, 8), (6, 6), (6, 5), (6, 3), (6, 2), (6, 8), (1, 6), (1, 5), (1, 3), (1, 2), (1, 8), (8, 6), (8, 5), (8, 3), (8, 2), (8, 8), (9, 6), (9, 5), (9, 3), (9, 2), (9, 8)]


# using List Comprehension
res1 = [(i,arin) for i in lst6 for arin in lst9]
print(res1)  # [(3, 6), (3, 5), (3, 3), (3, 2), (3, 8), (6, 6), (6, 5), (6, 3), (6, 2), (6, 8), (1, 6), (1, 5), (1, 3), (1, 2), (1, 8), (8, 6), (8, 5), (8, 3), (8, 2), (8, 8), (9, 6), (9, 5), (9, 3), (9, 2), (9, 8)]




# printf("ENter Number: ");
# scanf("%d",&num1);

# num1 = int(input("Enter one Number: "))  # default str
# num2 = int(input("Enter Second Number: "))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)   # return float value  # 10.5
# print(num1 // num2)   # return floor value   # 10


print("Hello Dhiraj Sir!", end = ' Arin BJP ')
print('Good Morning!')   # Hello Dhiraj Sir! Arin BJP Good Morning!


print("Arin","Mithil",'Noopur', sep=' 56 ')   # Arin    Mithil  Noopur


# ------------------------------------------------

# Prime Numbers

# 2,3,5,7,11,13,17,19,23,29.............

# 23 -> 1, 23   -> Divisors = 2   -> 23 % 1 == 0 -> true  /////   23 % 2 == 0 -> False   //   23 % 23  == 0
# 24 -> 1, 2, 3, 4, 6, 8, 12, 24 -> Divisors = 8


# min = int(input("Enter Minimum number: "))  # 10
# max = int(input("Enter Maximum number: "))  # 500

# counter = 0

# for j in range(min, max+1):   # 10 to 500   # j = 13
#     counter = 0
#     for i in range(1, j+1):   # 1 to 23    # i =  1 to 13
#         if j % i == 0:    #   13 % i == 0      
#             counter += 1    # (Assignment Operator -> Priority Low)  -> 6 + 2 = 8

#     if counter == 2:
#         print(j,end='\t')   # 11

num1 = int(input())
x = 2
v = 1
u = 1
sum = 0
print(x)  # 2
for i in range(1,num1):
    while v<=num1:
        u *= 10
        v+=1
    x = (x % u) * 10 + 2  # 44   # 2 * 10 + 2
    print(x)
    sum += x
sum += 2
print(sum)
# 24 -> 1,2,3,4,6,8,12,24
# 56 -> 1,2,4,7,8,14,28,56
# 23 -> 1,23
# 41 -> 1,41


# num = 23
# divisor = 0 
# counter = 0
# for i in range(1,num+1):
#     if num % i == 0:   # 24 % 1 == 0
#         print(i,end=' ')
#         counter += 1

# if counter == 2:
#     print("Prime")   # 1 23 Prime
# else:
#     print("Fail")


# num = 24
# flag = 0

# for i in range(2,num):  # 2 to 22
#     if num % i == 0:
#         flag = 1
#         break

# if flag == 1:
#     print("Not Prime")
# else:
#     print("Prime")

num = 44

# for i in range(2,num):  # 2 to 22
#     if num % i == 0:
#         break

# i = 2
# while i<num:    # 1 < 44   -> 1 to 43
#     if num % i == 0:   # 23 == 23
#         break
#     i+=1  # i = 44

# print(num)  # 44
# if num == i:  # 23 == 23
#     print("Prime")


# sum = 0
# mul = 1

# while num != 0:
#     rem = num % 10
#     sum = sum + rem
#     mul = mul * rem
#     num = num // 10

# if sum == mul:
#     print(True)


list1 = [[1,2,3],[4,5,6],[8,7,6]]

for i in range(3):   # 0,1,2   i = 2
    print("i = ",i)
    for j in range(0,i-1,-1):  #  j -> 0,1,-1
        print("j = ",j)
        print(list1[i][j])   # 1

# for i in list1: 
#     # print(i)   # [1, 2, 3]
#     for j in i:
#         print(j,end=' ')

tup1 = (1,4,5,6,7)
tup2 = (34,78,23,78,90)

# Tuple comprehension , Simple try
tup3 = (12, 56, 78)
tup3 += tup1
print(tup3)
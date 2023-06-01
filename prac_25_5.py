# dim = int(input("Enter Dimensions: "))   # 3

# matrix = []
# for i in range(dim):
#     x = [int(j) for j in input().split()]
#     matrix.append(x)

# print(matrix)


# l1 = [
#     [10,90,32],
#     [32,67,54],
#     [65,89,31]
# ]

# list1 = [10,20]

# list1[1] = 900
# list1[5] = 300
# print(list1)

list3 = []

list3 = [[], [], []]

tup1 = [(10,90,78,45), (32,4,5,63), (21,34,56,22), (44,3,21,1)]

# Second Highest Number ---> [78,32,34,21]

Que = [(23,90), (333,8), (21,90), (32, 782), (33,)]

ans = [(23,90), (21,90), (33,)]
k = 2
# Find k length ELement Pair from the list  # Lambda, Map

# ----------------------------

[(10,20,30), (55,32,90,32), (44,21,67,29,322)]

# Ans = [(10,20,30), (44,21,67,29,322), (55,32,90,32)]


# Dict, Set Comprehension

tup1 = [(10,90,78,45), 
        (32,4,5,63), 
        (21,34,56,22), 
        (44,3,21,1)]
list1 = []
for i in tup1:
    # print(i)   # (10, 90, 78, 45)
    x= sorted(i)
    # print(x)
    list1.append(tuple(x))

print(list1)


l3 = [10,20]

l3[1] = 900
# l3[5] = 78
print(l3)


tup1 = [(10,90,78,45), 
        (32,4,5,63), 
        (21,34,56,22), 
        (44,3,21,1)]

xerox = []
for i in tup1:
    xerox.append(list(i))
l1d = []

for i in tup1:
    for h in i:
        l1d.append(h)

l1d.sort()
k = 0
for i in range(len(tup1)):   # row
    for j in range(len(tup1[i])): # col
        xerox[i][j] = l1d[k]
        k+=1
print(xerox)

# --------------------------------

tup1.sort(key=lambda x : x[-2])
print(tup1)

l2 = [10,20,89,78,46,32]

num = int(input())
l2.sort()
for i in range(num):
    print(l2[i])

for j in range(len(l2) - num, len(l2)):
    print(l2[j])
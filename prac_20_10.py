
list1 = [4504, 1520, 5857,
4094
,4157
,3902
,822
,6643
,2422
,7288
,8245
,9948
,2822
,1784
,7802
,3142
,9739
,5629
,5413
,7232]
k = 5

list1.sort()

print(list1)   # [822, 1520, 1784, 2422, 2822, 3142, 3902, 4094, 4157, 4504, 5413, 5629, 5857, 6643, 7232, 7288, 7802, 8245, 9739, 9948]

diff = []
for i in range(len(list1)-4):  # 16  # 0 to 15
    temp = []
    for j in range(i,i+k):   # 0 to 4, 1 to 5  # 15 to 19
        temp.append(list1[j])
    print(temp)
    x = max(temp) - min(temp)
    diff.append(x)

print(diff)
print(min(diff))


# list1 = [i for i in range(1,5)]
# print(list1)


# Que - 1

list1 = ((10,90), (345,94), (10,456), (34,90), (567,90), (10,20,30))

k = 2

ans = ((10,90), (34,90), (10,20,30))


# Que - 2

list1 = [(10,20), (45, 33), (10,30,10), (33,45), (70,10), (33,70,10,45)]

ans = [(10,20,30), (45,33), (33,45,70,10), (70,10)]   # Simple, Comprehension
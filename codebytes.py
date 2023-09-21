# # dict1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

# # str1 = 'DLXIMVD'

# # sum = 0
# # for i in str1:
# #     sum+=dict1[i]

# # str2 = ''

# # val = [i for i in dict1.values()]
# # key1 = [i for i in dict1.keys()]
# # list1 = [[i,j] for i,j in dict1.items()]  


# # from bidict import bidict
# # dict2 = bidict(dict1)
# # dict3 = dict2.inverse

# # for key,j in dict1.items():
# #         if sum in val:
# #             str2 += dict3[sum]
# #             print(str2, '------')
# #             break

# #         for i in val[::-1]:
# #             if sum == 1:
# #                 str2 += 'I'
# #                 print(str2)
# #                 break
# #             if sum > i:
# #                 temp = i
# #                 break
# #         if sum == 1:
# #              break
        
# #         ans = sum / temp 

# #         if 1:
# #             ans = sum // temp

# #             for x,y in dict1.items():
# #                 if y == temp:
# #                     str2+= (x * ans)
            
# #                     break
           
# #             sum = sum % temp
# #             if sum == 0:
# #                 print(str2)
# #                 break
# #         if sum == 0:
# #                 print(str2)
# #                 break



# # sum = 3329
# # str1 = ''
# # while sum > 0:
# #     if sum >= 1000:
# #         str1 += 'M'
# #         sum -= 1000
# #         continue
    
# #     if sum >= 500:
# #         str1 += 'D'
# #         sum -= 500
# #         continue


# # j = 25
# # while j<=30:
# #     k= 25
# #     while k<=30:
# #         if j == k:
# #             k+=1
# #             continue
# #         print(k,end=' ')
# #         k+=1
# #     print(j,end=' ')
# #     j+=1


# a=[1,2,3,4,5,(4,5),"u",{"w":45,"r":21},5]
# # output
# # 1
# # 2
# # 3
# # 4
# # 5
# # tuple is: (4,5)
# # dictonary keys:w
# # dictonary values:45
# # dictonary keys:r
# # dictonary values:21
# # 5


# arr1 = [8,3,1]
# arr2 = [7,9,2]

# k = 10
# dict1 = {}
# new = []
# l1 = []

# for i in arr1:
#     l1 = []
#     for j in arr2:
#         if i+j >= 10:
#             l1.append(j)
#     arr2.remove(min(l1))

# if not arr2:
#     print('Yes')



def make_bricks(small, big, goal):
   
    if (big*5) > goal : 
        goal = goal % 5
    else:
        goal = goal - (5*big)   # goal = 46 - 5

    if small>=goal: 
        return True

    return False
    
# print(make_bricks(1,4,12))
print(make_bricks(3,2,8))
print(make_bricks(43,1,46))


list1 = [10,20]

list2 = list1.copy()   # Shallow Copy  Xerox

list1.append(900)
list2.append(600)

print(id(list1))
print(id(list2))

print(list1,list2)

list3 = list1
list3.append(400)
print(list1)
print(list3)   # Deep Copy

l5 = list(list3)   # Shallow Copy
l5.append(33)
print(list3) 


import copy

copy.copy()

m = [['T','s','i']
h%x
i #
sM 
$a 
#t%
ir!]]

row = 0
while row <= 6:
    col = 0
    while col <= 2:
        print()
        col+=1
    row+=1 
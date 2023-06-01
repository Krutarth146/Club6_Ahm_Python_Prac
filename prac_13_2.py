list1 = [1,2,3]
list2 = []

for i in list1:   # 3
    for j in range(0,i):     
        list2.append(i)
print(list2)

# 5. Write a Python function that checks whether a passed string is palindrome or not.

str2 = "Nayan"
flag=0
for i in range(0,len(str2)//2):
    if str2[i] != str2[len(str2)-i-1]:   # str2[0] == str2[4]  # N == n
        print("Not Palindrome")
        flag = 0
        break
    else:
        flag=1

if flag ==1:
    print("Palindrome")

# ----------------------------------







# 1. Take Nothing return Nothing
def priyank():
    a = 10
    b = 20  
    print(a+b)


priyank()   # 30



# 2. Take something return Nothing

def Diya(a,b,c=0):
    print(a+b+c)
    priyank()

Diya(10,20,90)  # 60



# 3. Take Nothing return something

def Henish():
    return 10

print(Henish())



# 4. Take something return something

# num = int(input())
# def Mahir(num):
#     for i in range(1,num+1):
#         yield i


# for h in Mahir(num):
#     print(h)
    

def Helly(id, name):
    print(id,name)

Helly(10,"Henish")




# Args
def Kalet(roll, *Fang):
    for j in Fang:
        print(j)


Kalet(10,20,304,"KL")



# Mississippi

# {'M' : 1, 'i' : 4 }

# kwargs

# Dictionary key, value pair

def Bhargi(**dict1):
    # print(kwargs.items())
    for i,j in dict1.items():
        print(j)


Bhargi(name = "Henish", address = "Ahm", id = 800, salary = 100) # dict_items([('name', 'Henush'), ('address', 'Ahm'), ('id', 800), ('salary', 100)])
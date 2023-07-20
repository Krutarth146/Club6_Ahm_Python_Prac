# virtual void royal() = 0;  in CPP

from abc import abstractmethod, ABC

class RBI(ABC):

    @abstractmethod
    def royal():  # blank Body
        pass

    def depositFD(self): 
        print("Good FD------------")

# henish = Bank()   #  Can't instantiate abstract class Bank with abstract method royal

class kotak(RBI):
    def royal(self):
        super().depositFD()   # 
        print('kotak Interest Rate: 7.0')
        # RBI.depositFD()
        # RBI.royal()

class HDFC(RBI):
    def royal(self):
        print('HDFC Interest Rate: 4.0')

class SBI(RBI):
    def royal(self):
        print('SBI Interest Rate: 2.5')


k1 = kotak()
h1 = HDFC()
k1.royal()
h1.royal()

# RBI.depositFD()

# r1=  RBI()


try:
    # r1 = RBI()
    # r1.depositFD()
    print(8/0)

except ZeroDivisionError:
    print("Zero Div. Error")


except Exception as err:
    print("interpreter Generated Error:",err)
    print("Don't Allowed to make object of abstract Class")
    k1.depositFD()

else:
    print("RBI class object is created")

finally:
    print("Always Executed")


l1 =  [(10,90), (232,21), (89,78), (21,22), (3,4)]
# ans = [(3,4) , ....]

l2 = [1,0,2,3,3,3,32,2,3,31,1,2,3]

# Ans = {1 : [0,10], 2 : [2,7,11] .....}



l1 =  [(10,90), (232,21), (89,78), (21,22), (3,4)]

for i in range(len(l1)-1): # 5   ---> 0 to 3
    for j in range(i+1, len(l1)):
        if l1[i][-1] > l1[j][-1]:
            # l1[i], l1[j] = l1[j], l1[i]
            safe = l1[i]
            l1[i] = l1[j]
            l1[j] = safe


print(l1)

# ------------------------------

def jayraj(tup1):
    return tup1[-1]

# print(jayraj((30,40,89,45)))

l1.sort(key=jayraj)

print(l1)

# a,b,c = 90,10,20


# ---------------------------------------

l2 = [1,0,2,3,3,3,32,2,3,31,1,2,3]

# Ans = {1 : [0,10], 2 : [2,7,11] .....}

dict1 = {}

unique = []

for i in l2:
    if i not in unique:
        unique.append(i)

# unique = list(set(l2))

for element in unique:  # i = 1
    temp = []
    for ind in range(len(l2)):
        if element == l2[ind]:
            temp.append(ind)  # [0,10]

    dict1[element] = temp

print(dict1)   # {1: [0, 10], 0: [1], 2: [2, 7, 11], 3: [3, 4, 5, 8, 12], 32: [6], 31: [9]}
print()
print()
print()
dict2 = {element : [ind for ind in range(len(l2)) if element == l2[ind]] for element in unique}
print(dict2)   # 120 Rs.
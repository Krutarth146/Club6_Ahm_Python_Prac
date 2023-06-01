set1 = {10,}

print(type(set1))  # class set

# dict1 = {key : value}

student = {'name' : "Krutarth", "roll" : 45, 89 : "Sargasan", "list1" : [90,90,89,78,67]}
print(student)  # {'name': 'Krutarth', 'roll': 45, 89: 'Sargasan'}

# key -> Unique

# Mutable
print(len(student))  # 3

print(type(student))  # <class 'dict'>

print(student.keys())  # dict_keys(['name', 'roll', 89, 'list1'])
print(student.values())  # dict_values(['Krutarth', 45, 'Sargasan', [90, 90, 89, 78, 67]])

print(student.items())  # dict_items([('name', 'Krutarth'), ('roll', 45), (89, 'Sargasan'), ('list1', [90, 90, 89, 78, 67])])

for i in student.items():
    print(i)

for i,j in student.items():
    print(i,j,sep='_',end='\t')


dict2 = {i:j for i,j in student.items()}
print(dict2)


fruit_list = {'apple' : 20.45, 'lichi' : 90.89, 'banana': 60.90, 'mango' : 45.0}

user_cart = [('apple',2), ('banana',7), ('lichi',5)]

# what is total bill amount?   # fruit_list['apple']
bill = 0
for i in user_cart:           # ('apple',2)
    if i[0] in fruit_list.keys():   # if 'apple' in ('apple','lichi','banana','mango')   # True
        bill += i[1] * fruit_list[i[0]]   # bill += 2 * 20.45

print(bill)  # 921.65    -> 40.9 + 426.3 + 454.45


for i in user_cart: # ('apple',2)
    for _ in i:
        print(_)  



# Dictionary COmprehension

set1 = {i for i in range(5)}
print(set1)  # {0, 1, 2, 3, 4}
print(type(set1))


index = [1,2,3,4,5]
name = ['a', 'mi', 'Si', 'wi', 'qi']

dict1 = {value:key for key,value in zip(index,name)}
print(dict1)   # {1: 'a', 2: 'mi', 3: 'Si', 4: 'wi', 5: 'qi'}
print(type(dict1))  # <class 'dict'>


dct2 = dict.fromkeys("n",'Henish')
print(dct2)


dct2 = dict.fromkeys(range(10),[10,30,405,90])
print(dct2)


list1 = [1,5,3,4,2]
cube = [(x,x**3) for x in list1]
print(cube)  # [(1, 1), (5, 125), (3, 27), (4, 64), (2, 8)]

cube1 = {l:l**3 for l in [45,2,1,4,56]}
print(cube1)   # {45: 91125, 2: 8, 1: 1, 4: 64, 56: 175616}
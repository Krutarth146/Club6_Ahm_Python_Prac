# Strings  -> Indexing / Slicing , String Methods
# char g='r';  char type
# char j[10] = "Royal";  (char type array means string)

str1 = "H"
print(type(str1))   # <class 'str'>

str2 = "Henish_is Good Student123."
print(type(str2))  # <class 'str'>

str3 = '45'
str4 = '45'
print(type(str3))   # <class 'str'>
print(str3+str4)    # 4545  (concat Operation)

str3 = int(str3)

print(str3 + int(str4))  # 90 (Type casting)

x = '91.89'
# print(int(x))   #  Gives Error

x = int(float(x))  # 91
print(x)   # 91

# Indexing and Slicing

str11 = "Henish_is Good Student123."
    #    012345678.....         -1
print(len(str11))   # 26 -> Length Strats from 1, Index starts from 0

print(str11[0])   # H
print(str11[5])   # h
print(str11[-2])   # 3
print(str11[-1])   # .
print(str11[-12])   #  (space is ans.)

# print(str11[start : end(n-1)])
print(str11[0 : 6])   # Henish
print(str11[4 : 5])   # s
print(str11[5 : 2])   # blank

str11 = "Henish_is Good Student123."
print(str11[-1 : 5])  # blank
print(str11[-5 : -2])  # t12
print(str11[-2 : -5])  # blank

print(str11[0:6:1])  # start : end(n-1) : step(n-1)  # Henish
print(str11[0:6:2])  # Hns
print(str11[5::1])  # h_is Good Student123.
print(str11[::4])  # Hssotn3
print(str11[::])  # Henish_is Good Student123.
print(str11[9:2:-1])  #  si_hsi
print(str11[7:1:-2])  # ihi
print(str11[::-1])  # .321tnedutS dooG si_hsineH
print(str11[:0:-1])  # .321tnedutS dooG si_hsine



# -----------------------------------------------

str11 = "Henish_Is Good Student123."
print(str11.capitalize())  # Henish_is good student123.
print(str11.casefold())   # henish_is good student123.
print(str11.lower())   # henish_is good student123.
print(str11.upper())   # HENISH_IS GOOD STUDENT123.
print(str11.swapcase())  # hENISH_iS gOOD sTUDENT123.
print(str11.title())   # Henish_Is Good Student123.
print(str11.istitle())  # True
print(len(str11))   # 26
print(str11.center(35,'*'))   # *****Henish_Is Good Student123.****

print(str11.count('o',11,12))   # 1

print(str11.encode())   # b'Henish_Is Good Student123.'


str45 = "Ståle"
print(str45.encode())  # b'St\xc3\xa5le'
print(str45.encode(encoding='ascii', errors= "namereplace")) # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str45.encode(encoding='ascii', errors= "replace")) # b'St?le'
print(str45.encode(encoding='ascii', errors= "xmlcharrefreplace")) # b'St&#229;le'
print(str45.encode(encoding='ascii', errors= "ignore")) # b'Stle'

print(str11.endswith('3.',5,27))  # True

str11 = "Henish_Is Good Student123."
# str11 = str11.expandtabs(12)  # Henish_Is Good          Student123.
# print(len(str11))  # 35
print(str11.find('Z'))  # -1  (Returns -1 if element is not found)
# print(str11.index('Z'))  # 10  # (Generates Error if element is not found)


print(str11.index('o'))  # 11
print(str11.rindex('o'))  # 12


str11 = "{name}_Is {mode} Student123.".format(name="Mahir",mode='Good')
print(str11)  # Mahir_Is Good Student123.


str11 = "{}_Is {} Student123.".format("Mahir",'Good')  # Mahir_Is Good Student123.
print(str11)

str11 = "{1}_Is {0} Student123.".format("Mahir",'Good')  # Mahir_Is Good Student123.
print(str11)  # Good_Is Mahir Student123.

a = 90
b = 80

print(f"Sum of {a} and {b} is {a+b}")  # Sum of 90 and 80 is 170  (fstring)

str90 = "_123"
print(str90.isalnum())   # True
print(str90.isalpha())   # False
print(str90.isascii())   # True
print(str90.isspace())   # False
print(str90.isdecimal())  # True
print(str90.isnumeric())  # True
print(str90.isdigit())   # True
print(str90.isidentifier())   # True
print(str90.isupper())  # False

str2 = "           Henish_is Good Student123.       "
print('_'.join(str2))
print(len(str2))   # 26
print(str2.ljust(30, '*'))   # Henish_is Good Student123.****
print(str2.rjust(30, '*'))   # ****Henish_is Good Student123.

print(str2.lower())   # henish_is good student123.
print(str2.lstrip())  # Henish_is Good Student123.
print(str2.rstrip())  #            Henish_is Good Student123.


str2 = "Henish_is Good Student123. hbk Henish school."  
print(str2.partition('Good'))  # ('Henish_is ', 'Good', ' Student123.')  # Total 3 parts
print(str2.partition(' '))  # ('Henish_is', ' ', 'Good Student123.')
print(str2.rpartition(' '))  # ('Henish_is Good Student123. hbk', ' ', 'school')

print(str2.split(' '))  # ['Henish_is', 'Good', 'Student123.', 'hbk', 'school']

print(str2.removeprefix('H'))  # enish_is Good Student123. hbk school.
print(str2.removesuffix('school.'))  # Henish_is Good Student123. hbk

# print(str2.replace('Henish', 'Maahir'))  # Maahir_is Good Student123. hbk school.
# print(str2.replace('Henish', 'Maahir', 1))  # Maahir_is Good Student123. hbk Henish school.

# str2[::-1]

# Henish_is good#Boy


# str3 = "Henish is good Boy"
# print(str2[::-1])
# str3 = str3[::-1]
# str3 = str3.replace(' ','#',1)
# str3 = str3[::-1]
# print(str3)   # Henish_is good#Boy
print(str2.replace('Henish','Mahir',1))
str2 = str2[::-1]
print(str2.replace('hsineH','Mahir',1))
str2 = str2[::-1]
print(str2)
print(str2.rfind('S'))  # 15

# print(str2.splitlines(''))

str78 = "Krutarth Daxeshbhai Patel"

list1 = str78.split(' ')
print(list1)

print(f"{list1[0][0]}.{list1[1][0]}.{list1[2]}")

print(str78.startswith('K'))  # True
print(str78.swapcase())  # kRUTARTH dAXESHBHAI pATEL

print(str78.title())  # Krutarth Daxeshbhai Patel

str87 = '7890'
print(str87.zfill(10))  # 0000007890

str90 = "Sam is God 123"
table = str90.maketrans('Sam' , 'Ram' , '123')
print(table)

print(str90.translate(table))   # Ram is God


# --------------------------------------------------

list1 = [10, 90,67,334 ,23]

for _ in list1:
    if _ % 2 != 0:
        print(_)

list2 = [_ for _ in list1 if _ % 2 != 0]
print(list2)  # [67, 23]

name = ['Henish', 'Mahir' , 'Helly']
upper1 = [n.upper() for n in name]
print(upper1)

lst4 = [1 ,2 ,3,4,5]
lst9 = [6,7,8,9,3,4]

# [(1,6), (1,7), (1,8).....]

for j in lst4:  # 1  2
    for k in lst9:  # 6 7 8 9 3 4
        print((j,k),end=' ')

lst8 = [(j,k) for j in lst4 for k in lst9]
print(lst8)


cube = [i**10 for i in lst9]
print(cube)

cube = [(i,i*i*i) for i in lst9]
print(cube)  # [(6, 216), (7, 343), (8, 512), (9, 729), (3, 27), (4, 64)]

list1 = [23, 89, 78, 56]
list2 = [99,89,78,11]


list3 = [i for i in zip(list1,list2) ]

print(list3)  # [(23, 99), (89, 89), (78, 78), (56, 11)]


for i in enumerate(list2):
    print(i)
lst4 = [i for i in enumerate(list2,100)]
print(lst4)

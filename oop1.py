# OOP 

# structure: ---> User defined Datatype

# class Student
# {
    # public:
#     int id;   # class Memebr Variables
#     char name[10];
#     float marks;

    # Student(id, name, marks)
    # {
    #     this->id = id;
    #     this->name = name;
    #     this->marks = marks;

    # }


#     void set_data()
#     {
#         id = 90;
#         marks = 800;
#     }

#     void display()
#     {
#         cout<<id<<name<<marks;
#     }

# };



# main()
# {
#             int       a;
#     struct Student   jay;
#            Student   Mahir;
# }
# Class ---> Blueprint
# objext -> Instance of Class


# Constructor  ---> To Intialize member Variables
# Student()
# {

# }

# (self ---> this keyword in Java & CPP)

class Student:
    ROI = 7   # Class Variable

    # def __init__(self):
    #     self.id = int(input())   # Instance Variable
    #     self.name = input()      # Instance Variable
    #     self.marks = int(input()) # Instance Variable
    def __init__(self):
        self.id = 10   # Instance Variable
        self.name = "Ashok"      # Instance Variable
        self.marks = 400 # Instance Variable

# Student s1;  in CPP

maahir = Student()
henish = Student()
# print(type(maahir))   # <class '__main__.Student'>

print(maahir.marks)   # 200
print(henish.id)    # 20

print(maahir.ROI)   # 7
print(henish.ROI)   # 7
print(Student.ROI)   # 7

maahir.school = "HBK"
print(maahir.school)

# maahir.ROI = 90

# print(maahir.ROI)   # 90
# print(henish.ROI)   # 7
# print(Student.ROI)   # 7


Student.ROI = 88

print(maahir.ROI)   # 88
print(henish.ROI)   # 88
print(Student.ROI)   # 88
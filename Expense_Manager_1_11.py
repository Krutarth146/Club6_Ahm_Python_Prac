class Customer:
    def __init__(self):
        # Personal Details
        self.name = ""
        self.email = ""
        self.password = ""

        # Expense Details
        self.grocerry = 0
        self.utility = 0
        self.other = 0

    def Signup(self):   # Instance Method
        email = input("Enter Email: ")
        if email.count('@') == 1 and email.endswith('.') == False and email.count('@.') == 0:
            self.email = email
            self.name = input("Enter Name: ")
            self.password = input('Enter Password: ')
            # Validation (min  1 Capital Alpha, 1 Small, 1 Numerical, 1 Special Character) ----> Regex
            return 1
        else:
            return 0
        
    def login(self,userid, password):
        return self.email == userid and self.password == password
    

    def G_Exp(self, amount):
        if amount > 0:
            self.grocerry += amount

    def U_Exp(self,amount):
        if amount > 0:
            self.utility += amount

            
    def O_Exp(self,amount):
        if amount > 0:
            self.other += amount


list1 = []   # for storing all person's Data


while -10:   # True
    print("1 --- Signup")
    print("2 --- Login")
    print("3 --- Show Customers")
    print("4 --- Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        c = Customer()   # New Person  Blank 6 Boxes 
        if c.Signup():  # Data Load  6 ---> 3 Box Full
            list1.append(c)   # list1 = [person1]

    elif choice == 2:
        e = input("Enter User Id: ")
        p = input('Enter Password: ')

        for obj in list1:
            flag = 0   
            if obj.login(e,p):
                flag = 1
                print(f"Hello {obj.name}! Welcome to Expense Management System")
                while True:
                    print("1 --- Grocerry Expense")
                    print("2 --- Utility Expense")
                    print("3 --- Other Expense")
                    print("4 --- Show Expenses")
                    print("5 --- Back to Dashboard")

                    Ex_choice= int(input("Enter Expense Choice: "))

                    if Ex_choice == 1:
                        obj.G_Exp(int(input("Enter any amount: ")))

                    elif Ex_choice == 2:
                        obj.U_Exp(int(input("Enter any amount: ")))

                    elif Ex_choice == 3:
                        obj.O_Exp(int(input("Enter any amount: ")))

                    elif Ex_choice == 4:
                        print(obj.grocerry, obj.utility, obj.other)
                        print("Sum =",obj.grocerry + obj.utility + obj.other)

                    elif Ex_choice == 5:
                        break
                break

        if flag == 0:
            print("Cred. Invalid, Back to Login Press 2")


    elif choice == 3:
        for x in list1:
            print(x.name)

    elif choice== 5:
        exit()
    
# Email Duplication, Password Validation, Storage Problem (file/Json or mysql)
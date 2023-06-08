class Bank:
    bank_employee = 5
    _ROI = 9  # Class Variable
    __tressury = 9000000

    def __init__(self):
        self.name = None
        self.balance = 0

    def create_new(self):   # Instance Method
        self.name = input()

    def add_deposit(self, money):
        if money > 0:
            self.balance += money
        return self.balance
    
    def withdraw(self, money):
        if money < 0 or (self.balance - money) < 5000:
            print("Not Allowed")
        else:
            self.balance -= money
        return self.balance
    
    
    def show_bal(self):
        print(f"Your Balance is {self.balance}")  # fstring
    
    @classmethod
    def Increse_ROI(cls):
        cls._ROI += 2
        print("Interest Rates are Updated!!")

    @staticmethod
    def show_loan_interest():
        b2 = Bank()
        b2._ROI = 80
        print(b2._ROI)

    def give_interest(self):
        self.balance += ((self.balance * self._ROI) / 100)


manoj = Bank()

manoj.create_new()
manoj.add_deposit(10000)
manoj.show_bal()
manoj.withdraw(8000)
manoj.withdraw(2000)
manoj.show_bal()
manoj.Increse_ROI()
manoj.give_interest()
manoj.show_bal()

manoj.show_loan_interest()  # 11

# print(Bank._ROI)  # 11

# Bank.ROI = 15
# print(Bank.ROI)  # 15

# print(Bank.__tressury)
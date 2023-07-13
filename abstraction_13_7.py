# virtual void royal() = 0;  in CPP

from abc import abstractmethod, ABC

class RBI(ABC):

    @abstractmethod
    def royal():  # balnk Body
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
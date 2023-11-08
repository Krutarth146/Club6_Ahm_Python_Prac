import mysql.connector

mydb = mysql.connector.connect(user="root", password = "mysql", database = "club6", host="localhost")


if mydb.is_connected():
    print("Database Connected....")
else:
    print("Error Occured")


cur = mydb.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS CUST_DETAILS (ID INT(4) AUTO_INCREMENT, NAME VARCHAR(30) NOT NULL, MOB_NUMBER INT(10) NOT NULL, JOIN_DATE DATE NOT NULL, SUBS_END_DATE DATE NOT NULL, PRIMARY KEY(ID,NAME))")

# # DEFAULT --- DUE

# cur.execute("CREATE TABLE IF NOT EXISTS PHY_DETAILS (ID INT(4), NAME VARCHAR(30), HEIGHT FLOAT NOT NULL, CUR_WEIGHT FLOAT NOT NULL, BMI FLOAT NOT NULL, TARGET_WEIGHT FLOAT NOT NULL, FOREIGN KEY (ID,NAME) REFERENCES CUST_DETAILS(ID,NAME))")

# cur.execute("CREATE TABLE IF NOT EXISTS CRED (ID INT(4), NAME VARCHAR(30) NOT NULL, USER_ID VARCHAR(30) NOT NULL, PASSWORD VARCHAR(30) NOT NULL, ENTER_TIME TIME NOT NULL, EXIT_TIME TIME NOT NULL, ENTER_WEIGHT FLOAT NOT NULL, EXIT_WEIGHT FLOAT NOT NULL, FOREIGN KEY (ID,NAME) REFERENCES CUST_DETAILS(ID,NAME))")


# cur.execute("ALTER TABLE CUST_DETAILS ADD GENDER CHAR NOT NULL")


from datetime import datetime


class wrongPassword(Exception):
    pass

class subsEnd(Exception):
    pass

class UserIdExists(Exception):
    pass

try:
    print("1 ----- Signup")
    print("2 ----- Login")
    print("3 ----- Logout")
    print("4 ----- Sub. Renewal")

    choice = int(input("Enter Your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        contact = int(input("Enter Mobile No: "))
        gender = input("Enter Gender: ")
        userId = input("Enter User ID: ")   # Alter Query  (Unique, Not null)
        password = input("Enter Password: ")
        joining = datetime.today()
        cur.execute("select DATE_ADD(SYSDATE(), INTERVAL 1 YEAR) FROM DUAL")
        renewal = cur.fetchone()  # (2024-05-22,)

        query = "INSERT INTO CUST_DETAILS (NAME, MOB_NUMBER, JOIN_DATE, SUBS_END_DATE, GENDER) VALUES (%s, %s, %s, %s, %s)"
        tup1 = (name, contact, joining, renewal[0], gender)
        cur.execute(query, tup1)

        query = "INSERT INTO CRED (NAME, ) VALUES (%s, %s, %s, %s, %s)"
        tup1 = (name, contact, joining, renewal[0], gender)
        cur.execute(query, tup1)

        height = float(input("Enter Height: "))
        weight = float(input("Enter Weight: "))
        BMI = weight / (height / 100)
        target = 60 # Google formula  
        que = "INSERT INTO PHY_DETAILS (HEIGHT, CUR_WEIGHT, BMI, TARGET_WEIGHT) VALUES (%s, %s, %s, %s)"
        val = (height, weight, BMI, target)
        cur.execute(que, val)
        mydb.commit()

    elif choice == 2:
        user_id = input("Enter User ID: ")  # maahir007
        cur.execute("SELECT USER_ID, PASSWORD FROM SAMPLE WHERE NAME = %s".format(user_id))
        x = cur.fetchone()
        # x = cur.fetchall()


        if len(x) == 0:
            print("No record Found")
        else:
            while 40:
                try: 
                    password =  input("Enter Password: ")
                    cur.exceute("SELECT USER_ID FROM SAMPLE")
                    x = cur.fetchall()  # [('Mahir',), ('Henish', )]

                    for i in x:
                        if i[0] == password:
                            raise UserIdExists
                
                except UserIdExists:
                    print("User id Already Exists.. Please Choose another")


except:
    print("Error")




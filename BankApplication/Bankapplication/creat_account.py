import random
import banking
import conection
import mysql.connector


ac = 0

def create_account():
    print"Please enter your details:"
    name=raw_input("Name:")
    ad=raw_input("Address:")
    ph =raw_input("Contact number:")
    ph = ph.replace("-","")
    # cheking for validity of the phone number
    if len(ph) != 10:
        print "Not a valid US phone number! eg: 3104671146"
        create_account()
    bal = float(raw_input("Amount of money you want to deposit today:"))
    ac = random.randrange(10000, 100000)
    pin = random.randint(1000, 9999)
    try:
        cn = conection.connector()
        cursor = cn.cursor()
        query = ("INSERT INTO customer VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')").format(ac,pin,name,ad,ph,bal)
        cursor.execute(query)
        cn.commit()
        print "Your Account has been created."

    except mysql.connector.errors.ProgrammingError as e:
        print e
    finally:
        cursor.close()
        cn.close()


    ex = int(raw_input("Do you want to exit? 1. Yes , 2. No"))
    if (ex == 1):
        print "Have a nice day!"
        exit()
    else:
        banking.welcome_page()


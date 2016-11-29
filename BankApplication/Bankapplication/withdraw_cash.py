import banking
import conection
import mysql.connector
from decimal import Decimal

pin1 =0
counter = 3;


def withdraw():
    ac = raw_input("Please enter your account number:")
    pin = raw_input("Please enter your pin number:")
    try:
        cn = conection.connector()
        cursor = cn.cursor()
        query = ("select pin from customer where accountno={0};").format(ac)
        cursor.execute(query)
        row = cursor.fetchone()
        pin1 = row[0]
        if pin1 == int(pin):
            query1 = ("select bal from customer where accountno={0};").format(ac)
            cursor.execute(query1)
            row = cursor.fetchone()
            bal = row[0]
            bal1 =raw_input("Please enter the amount of money you want to withdraw today:")
            if Decimal(bal1) <= Decimal(bal) :
                bal  = bal - Decimal(bal1)
            else:
                print"you cannot withdraw more than your current bal."
                withdraw()
            query2 = ("UPDATE customer SET bal = '{0}' WHERE accountno = {1};").format(bal,ac)
            cursor.execute(query2)
            cn.commit()
            print "Your current balance is :", bal
        else:
            global counter
            while (counter > 0):
                print"credentials wrong, please try again."
                counter = counter - 1
                print counter
                withdraw()
            else:
                print"Sorry u have typed your pin wrong more than 3 times"
                exit()
    except mysql.connector.errors.ProgrammingError as e:
        print e
    finally:
        cursor.close()
        cn.close()

    ex = int(raw_input("Do you want to exit? 1. Yes , 2. No"))
    if(ex==1):
        print "Have a nice day!"
        exit()
    else:
        banking.welcome_page()



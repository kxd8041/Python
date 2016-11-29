import banking
import conection
import mysql.connector


pin1 =0
counter = 3;


def checkbal():

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
            print "Remaining Balance :",row[0]
        else:
            global counter
            while (counter > 0):
                print"credentials wrong, please try again."
                counter = counter - 1
                print counter
                checkbal()
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



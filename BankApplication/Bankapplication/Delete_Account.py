import banking
import conection
import mysql.connector


def delete():
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
            query2 = ("DELETE FROM customer WHERE accountno={0};").format(ac)
            cursor.execute(query2)
            cn.commit()
            print "Your Account has been deleted"
        else:
            global counter
            while (counter > 0):
                print"credentials wrong, please try again."
                counter = counter - 1
                print counter
                delete()
            else:
                print"Sorry u have typed your pin wrong more than 3 times"
                exit()
    except mysql.connector.errors.ProgrammingError as e:
        print e
    finally:
        cursor.close()
        cn.close()
    print "Thank you for letting us serve you."
    exit()

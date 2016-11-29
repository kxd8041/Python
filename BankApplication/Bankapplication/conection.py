from time import sleep
import mysql.connector
import configparser




def connector():
    try:
        config = configparser.RawConfigParser()
        config.read('config.cfg')
        user = config.get("user1", "user")
        password = config.get("user1","password")
        host = config.get("user1","host")
        database = config.get("user1","database")
        cn = mysql.connector.connect(user=user, password=password, host=host,
                                     database=database)
    except mysql.connector.Error as e:
        if e.errno==1045:
            print('Please check your credentials')
        if e.errno==1049:
            print('There is no such Database')
        if e.errno==2012|2013|2006|2046:
            reconnect()
        print "Error Found, Please try again after some time:"
        print e
    return cn


def reconnect():
    print"Server is down, We will try to connect you back in some time"
    sleep (100)
    connector()
    return



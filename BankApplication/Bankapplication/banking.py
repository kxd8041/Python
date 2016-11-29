"""
# Author :Krishna teja
# Simple Bank application using file system as a database having the functionalities of
# Create account, Check balance, Withdraw cash, Deposit cash, and delete account.
"""
import creat_account
import Delete_Account
import check_balance
import deposit_cash
import withdraw_cash


def welcome_page():
    print " Welcome to the Bank"
    print " How can we help to you Today"

    print"  {0}. Create Account".format(1)
    print"  {0}. Check Balance".format(2)
    print"  {0}. Withdraw Cash".format(3)
    print"  {0}. Deposit Cash".format(4)
    print"  {0}. Delete Account".format(5)

    s = int(raw_input("Please choose an option"))

    if (s==1):
        creat_account.create_account()
    elif(s==2):
        check_balance.checkbal()
    elif(s==3):
        withdraw_cash.withdraw()
    elif(s==4):
        deposit_cash.deposit()
    elif(s==5):
        Delete_Account.delete()
    else:
        print "Please choose from the given options or contact the helpline"
        welcome_page()

welcome_page()
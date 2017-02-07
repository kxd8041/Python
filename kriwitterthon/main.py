from twython import Twython,TwythonError
import configparser
from flask import Flask
from flask import render_template
import app

app = Flask(__name__)


class kriwitterthon(object):

    def __init__(self):
        print"hi"
        Config = configparser.ConfigParser()
        Config.read('t.ini')
        APP_KEY = Config.get('File_APP_Info', 'APP_KEY')
        APP_SECRET = Config.get('File_APP_Info', 'APP_SECRET')

        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

    def Welcome_Message(self):

        print("Welcome to the Application:")

        print"  {0}. Retrieving tweets of a particular User".format(1)
        print"  {0}. Retrieving followers of a particular User".format(2)
        print"  {0}. Retrieving Similar followers of two different User".format(3)
        print"  {0}. Searching a specific tweet".format(4)
        print " "
        s = int(raw_input("Please choose an option"))
        print " "

        if (s == 1):
            user = raw_input("Please enter a valid twitter screen name:")
            print " "
            k.Getting_Tweets(user)
        elif (s == 2):
            user = raw_input("Please enter a valid twitter screen name:")
            print " "
            k.Getting_Followers(user)
        elif (s == 3):
            user = raw_input("Please enter a valid twitter screen name:")
            user2 = raw_input("Please enter another valid twitter screen name:")
            print " "
            k.Getting_Similar_Followers(user,user2)
        elif (s == 4):
            user = raw_input("Please enter a valid twitter screen name:")
            string = raw_input("Please enter a string to search tweets containing the string:")
            print " "
            k.Searching_Tweet(string,user)
        else:
            print "Please choose from the given options or contact the helpline"
            k.Welcome_Message()

    @app.route('/')
    def Getting_Tweets(self):

        try:
            val=[]
            for i in range(0, 10):
                user_timeline = twitter.get_user_timeline(screen_name= "krish1092",count=10)
                for twitteruser in user_timeline:
                     val.append(twitteruser['text'])
                print val
            return val
            return render_template('kriwitterthon.html',val)


        except TwythonError as e:
            print e

    def Getting_Followers(self,user):

        try:
            next_cursor = -1
            while next_cursor !=0 :
                output = self.twitter.get_followers_list(screen_name=user, count=200, cursor = next_cursor)

                for twitteruser in output["users"]:
                    print(twitteruser["screen_name"])
                    next_cursor = output["next_cursor"]


        except TwythonError as e:
            print e

    def Getting_Similar_Followers(self,user,user2):

        try:
            output = self.twitter.get_followers_ids(screen_name=user)
            output2 = self.twitter.get_followers_ids(screen_name=user2)

            for twitteruser1 in output["ids"]:
                for twitteruser2 in output2["ids"]:
                    data = self.twitter.show_user(user_id=twitteruser1)
                    data2 = self.twitter.show_user(user_id=twitteruser2)
                    if data == data2:
                        print(data["screen_name"])
        except TwythonError as e:
            print e

    def Searching_Tweet(self,string,user):


        try:
            output = self.twitter.get_user_timeline(screen_name=user)

            for twitteruser in output:
                if string in twitteruser['text']:
                    print twitteruser['text']
        except TwythonError as e:
            print e


            ## get user timeline





k = kriwitterthon()
#k.Welcome_Message()
app.run()
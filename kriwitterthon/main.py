from twython import Twython,TwythonError
import linecache
import os




class kriwitterthon(object):

    def __init__(self):
        loc = os.getcwd() + "/t.txt"

        APP_KEY = "W3vcoOKqpj53QXZQZf0SXgkjz"
        APP_SECRET = linecache.getline(loc, 2).rstrip()

        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        self.twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)



    def gettingMessages(self):

        user=raw_input("Please enter a valid twitter screen name:")
        try:
            for i in range(0, 10):
                user_timeline = self.twitter.get_user_timeline(screen_name=user,count=10)
                for tweet in user_timeline:
                    print tweet['text']
        except TwythonError as e:
            print e

    def gettingUsers(self):

        user=raw_input("Please enter a valid twitter screen name:")


        try:
            output = self.twitter.get_followers_ids(screen_name=user)
            for x in output["ids"]:
                data = self.twitter.show_user(user_id=x)
                print(data["screen_name"])
        except TwythonError as e:
            print e

    def gettingsimilarUser(self):

        user = raw_input("Please enter a valid twitter screen name:")
        user2 = raw_input("Please enter another valid twitter screen name:")

        try:
            output = self.twitter.get_followers_ids(screen_name=user)
            output2 = self.twitter.get_followers_ids(screen_name=user2)

            for x in output["ids"]:
                for y in output2["ids"]:
                    data = self.twitter.show_user(user_id=x)
                    data2 = self.twitter.show_user(user_id=y)
                    if data ==data2:
                        print(data["screen_name"])
        except TwythonError as e:
            print e

    def searchingTweet(self):


        user = raw_input("Please enter a string to search tweets containing the string:")
        try:
            output = self.twitter.search(q=user)

            print output
            for tweet in output['statuses']:
                print tweet['text']
        except TwythonError as e:
            print e





k= kriwitterthon()
k.gettingMessages()
k.gettingUsers()
k.gettingsimilarUser()
k.searchingTweet()

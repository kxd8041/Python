from twython import Twython,TwythonError
import linecache
import os




class kriwitterthon(object):


    def gettingmessages(self):
        loc = os.getcwd() + "/t.txt"

        APP_KEY = "W3vcoOKqpj53QXZQZf0SXgkjz"
        APP_SECRET = linecache.getline(loc, 2).rstrip()

        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

        user=raw_input("Please enter a valid twitter screen name:")
        try:
            for i in range(0, 10):
                user_timeline = twitter.get_user_timeline(screen_name=user,count=10)
                for tweet in user_timeline:
                    print tweet['text']
        except TwythonError as e:
            print e

    def gettingUsers(self):
        loc = os.getcwd() + "/t.txt"
        APP_KEY = "W3vcoOKqpj53QXZQZf0SXgkjz"
        APP_SECRET = linecache.getline(loc, 2).rstrip()

        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

        user=raw_input("Please enter a valid twitter screen name:")
        output = twitter.get_followers_ids(screen_name=user)

        for x in output["ids"]:
            data = twitter.show_user(user_id=x)
            print(data["screen_name"])

    def gettingsimilarUser(self):
        loc = os.getcwd() + "/t.txt"
        APP_KEY = "W3vcoOKqpj53QXZQZf0SXgkjz"
        APP_SECRET = linecache.getline(loc, 2).rstrip()

        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

        user = raw_input("Please enter a valid twitter screen name:")
        output = twitter.get_followers_ids(screen_name=user)
        user2 = raw_input("Please enter another valid twitter screen name:")
        output2 = twitter.get_followers_ids(screen_name=user)

        for x in output["ids"]:
            for y in output2["ids"]:
                data = twitter.show_user(user_id=x)
                data2 = twitter.show_user(user_id=y)
                if data ==data2:
                    print(data["screen_name"])





    #gettingmessages(1)
    #gettingUsers(1)
    #gettingsimilarUser(1)

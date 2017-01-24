from twython import Twython,TwythonError
import linecache
import os

loc=os.getcwd()+"/t.txt"
print linecache.getline(loc,2).rstrip()



class kriwitterthon(object):
    def gettingmessages(self):

        APP_KEY = "W3vcoOKqpj53QXZQZf0SXgkjz"


        APP_SECRET = "a7iw3LspHUVQ5UvcIJG5q8Uh9obPs9VdvzcKCKfifpVwFIkq6K"

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

    gettingmessages(1)
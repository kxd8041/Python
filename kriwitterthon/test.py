import configparser
from twython import Twython,TwythonError
from flask import Flask,jsonify
app = Flask(__name__)

Config = configparser.ConfigParser()
Config.read('t.ini')
APP_KEY = Config.get('File_APP_Info', 'APP_KEY')
APP_SECRET = Config.get('File_APP_Info', 'APP_SECRET')

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


@app.route('/')
def hello_world():

    val = []
    for i in range(0, 10):
        user_timeline = twitter.get_user_timeline(screen_name="krish1092", count=10)
        for twitteruser in user_timeline:
            val.append(twitteruser['text'])

    return jsonify(result= val )

@app.route('/1')

def Getting_Followers():
    try:
        val =[]
        next_cursor = -1
        while next_cursor != 0:
            output = twitter.get_followers_list(screen_name="krish1092", count=200, cursor=next_cursor)

            for twitteruser in output["users"]:
                val.append(twitteruser["screen_name"])
                next_cursor = output["next_cursor"]
            return jsonify(result=val)




    except TwythonError as e:
        print e


@app.route('/2')

def Getting_Similar_Followers():
    try:
        val = []
        output = twitter.get_followers_ids(screen_name="krish1092")
        output2 =twitter.get_followers_ids(screen_name="krish1092")

        for twitteruser1 in output["ids"]:
            for twitteruser2 in output2["ids"]:
                data = twitter.show_user(user_id=twitteruser1)
                data2 = twitter.show_user(user_id=twitteruser2)
                if data == data2:
                    val.append(data)
        return jsonify(result=val)
    except TwythonError as e:
        print e
        

@app.route('/3')

def Searching_Tweet():
    try:
        val = []
        output = twitter.get_user_timeline(screen_name="krish1092")

        for twitteruser in output:
            if "adi" in twitteruser['text']:
                val.append(twitteruser['text'])
        return jsonify(result=val)

    except TwythonError as e:
        print e


app.run()
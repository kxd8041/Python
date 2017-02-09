import configparser
from twython import Twython,TwythonError
from flask import Flask,jsonify,request, redirect, render_template
app = Flask(__name__)

Config = configparser.ConfigParser()
Config.read('t.ini')
APP_KEY = Config.get('File_APP_Info', 'APP_KEY')
APP_SECRET = Config.get('File_APP_Info', 'APP_SECRET')

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

@app.route('/')
def index():
    return render_template('kriwitterthon.html')



@app.route('/', methods = ['POST'])
def Getting_Tweets():

    val = []
    user = request.form['user']
    print user
    for i in range(0, 10):
        user_timeline = twitter.get_user_timeline(screen_name=user, count=10)
        for twitteruser in user_timeline:
            val.append(twitteruser['text'])

    return jsonify(result= val )

@app.route('/', methods = ['POST'])

def Getting_Followers():
    try:
        user = request.form['user1']
        print user
        val =[]
        next_cursor = -1
        while next_cursor != 0:
            output = twitter.get_followers_list(screen_name=user, count=200, cursor=next_cursor)

            for twitteruser in output["users"]:
                val.append(twitteruser["screen_name"])
                next_cursor = output["next_cursor"]
        return jsonify(result=val)




    except TwythonError as e:
        print e


@app.route('/', methods = ['POST'])

def Getting_Similar_Followers():
    try:
        user = request.form['user2']
        print "hi"
        val = []
        output = twitter.get_followers_ids(screen_name= user)
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
        

@app.route('/', methods = ['POST'])

def Searching_Tweet():
    try:
        user = request.form['user3']
        string = request.form['string']
        print user, string
        print 'hi'

        val = []
        output = twitter.get_user_timeline(screen_name=user)

        for twitteruser in output:
            if string in twitteruser['text']:
                val.append(twitteruser['text'])
        return jsonify(result=val)

    except TwythonError as e:
        print e


if __name__ == '__main__':
    app.run()
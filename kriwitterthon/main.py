import logging
import datetime
import configparser
from twython import Twython, TwythonError
from flask import Flask, jsonify, request, redirect, render_template

app = Flask(__name__)

# Creating the Log File based on the date, so that each day has a different log file.
name = str(datetime.date.today()) + ".log"
logging.basicConfig(filename=name, level=logging.DEBUG)

# Creating the config parser object and getting the app keys from files.
Config = configparser.ConfigParser()
Config.read('t.ini')
APP_KEY = Config.get('File_APP_Info', 'APP_KEY')
APP_SECRET = Config.get('File_APP_Info', 'APP_SECRET')

# Creating Twython object using the app keys.
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


# Creating  routes to different HTML files to access different methods.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Tweets')
def aFunc():
    return render_template('kriwitterthon.html')

@app.route('/Followers')
def aFunc1():
    return render_template('1.html')


@app.route('/SimilarFollowers')
def aFunc2():
    return render_template('2.html')


@app.route('/SpecificTweet')
def aFunc3():
    return render_template('3.html')

@app.route('/TweetResult')
def aFunc4():
    return render_template('result.html')

@app.route('/FollowersResult')
def aFunc5():
    return render_template('result.html')

@app.route('/SimilarFollowersResult')
def aFunc6():
    return render_template('result.html')

@app.route('/SpecificTweetResults')
def aFunc7():
    return render_template('result.html')




# Method to get the most recent tweets of a particular user using their twitter handle.
@app.route('/TweetResult', methods=['POST'])
def Getting_Tweets():
    try:
        val = []
        user = request.form['user']
        logging.info('The Twitter Handle used is', user)
        logging.debug('The Twitter Handle used is', user)
        user_timeline = twitter.get_user_timeline(screen_name=user, count=10)

        for twitteruser in user_timeline:
            val.append(twitteruser['text'])

        return render_template('result.html',x=val)




    except TwythonError as e:
        logging.info(e)
        print e


# Method to get Followers of a particular user using their twitter handle.
@app.route('/FollowersResult', methods=['POST'])
def Getting_Followers():
    user = request.form['user1']

    try:
        val = []
        next_cursor = -1
        logging.debug('The Twitter Handle used is', user)

        while next_cursor != 0:
            output = twitter.get_followers_list(screen_name=user, count=200, cursor=next_cursor)
            # logging.debug('The Twitter Handle used is',user)

            for twitteruser in output["users"]:
                val.append(twitteruser["screen_name"])
                next_cursor = output["next_cursor"]
        return render_template('result.html',x=val)




    except TwythonError as e:
        logging.info(e)
        print e


# Method to get Similar followers of two user's using their twitter handles.
@app.route('/SimilarFollowersResult', methods=['POST'])
def Getting_Similar_Followers():
    user = request.form['user2']
    user2 = request.form['user3']
    logging.debug('The Twitter Handle used is', user)
    logging.debug('The Twitter Handle used is', user2)

    try:

        val = []
        output = twitter.get_followers_ids(screen_name=user)
        output2 = twitter.get_followers_ids(screen_name=user2)

        for twitteruser1 in output["ids"]:
            for twitteruser2 in output2["ids"]:
                data = twitter.show_user(user_id=twitteruser1)
                data2 = twitter.show_user(user_id=twitteruser2)
                if data == data2:
                    val.append(data)
        return render_template('result.html',x=val)

    except TwythonError as e:
        logging.info(e)
        print e


# Method to search a particular tweet of a particular user using their twitter handle and search key word.
@app.route('/SpecificTweetResults', methods=['POST'])
def Searching_Tweet():
    user = request.form['user4']
    string = request.form['string']
    logging.debug('The Twitter Handle used is', user)
    logging.debug('The Twitter Handle used is', string)

    try:

        val = []
        output = twitter.get_user_timeline(screen_name=user)

        for twitteruser in output:
            if string in twitteruser['text']:
                val.append(twitteruser['text'])

        return render_template('result.html',x=val)

    except TwythonError as e:
        logging.info(e)
        print e


# starting the app
if __name__ == '__main__':
    app.run()
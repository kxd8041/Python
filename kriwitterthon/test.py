import configparser
from twython import Twython,TwythonError
from flask import Flask,jsonify,request, redirect, render_template
app = Flask(__name__)
import logging


logging.basicConfig(filename='example.log',level=logging.DEBUG)


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

@app.route('/1')
def aFunc1():
    return render_template('1.html')

@app.route('/2')
def aFunc2():
    return render_template('2.html')

@app.route('/3')
def aFunc3():
    return render_template('3.html')



@app.route('/', methods = ['POST'])
def Getting_Tweets():

    try:
        val = []
        user = request.form['user']
        logging.debug('The Twitter Handle used is', user)
        for i in range(0, 10):
            user_timeline = twitter.get_user_timeline(screen_name=user, count=10)

            for twitteruser in user_timeline:
                val.append(twitteruser['text'])

        return jsonify(result= val )

    except TwythonError as e:
        logging.info(e)



@app.route('/1', methods = ['POST'])
def Getting_Followers():
    user = request.form['user1']

    try:
        val =[]
        next_cursor = -1
        logging.debug('The Twitter Handle used is', user)

        while next_cursor != 0:
            output = twitter.get_followers_list(screen_name=user, count=200, cursor=next_cursor)
            logging.debug('The Twitter Handle used is',user)

            for twitteruser in output["users"]:
                val.append(twitteruser["screen_name"])
                next_cursor = output["next_cursor"]
        return jsonify(result=val)




    except TwythonError as e:
        logging.info(e)


@app.route('/2', methods = ['POST'])


def Getting_Similar_Followers():
    user = request.form['user2']
    user2 = request.form['user3']
    logging.debug('The Twitter Handle used is', user)
    logging.debug('The Twitter Handle used is', user2)


    try:

        val = []
        output = twitter.get_followers_ids(screen_name= user)
        output2 =twitter.get_followers_ids(screen_name=user2)

        for twitteruser1 in output["ids"]:
            for twitteruser2 in output2["ids"]:
                data = twitter.show_user(user_id=twitteruser1)
                data2 = twitter.show_user(user_id=twitteruser2)
                if data == data2:
                    val.append(data)
        return jsonify(result=val)
    except TwythonError as e:
        logging.info(e)
        

@app.route('/3', methods = ['POST'])

def Searching_Tweet():
    user = request.form['user3']
    string = request.form['string']
    logging.debug('The Twitter Handle used is', user)
    logging.debug('The Twitter Handle used is', string)

    try:


        val = []
        output = twitter.get_user_timeline(screen_name=user)

        for twitteruser in output:
            if string in twitteruser['text']:
                val.append(twitteruser['text'])
        return jsonify(result=val)

    except TwythonError as e:
        logging.info(e)


if __name__ == '__main__':
    app.run()
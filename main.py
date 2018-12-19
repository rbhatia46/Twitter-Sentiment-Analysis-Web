from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'h8MAWmQjRq0dX1DWi670SoYbl'
consumer_secret = 'vAumwZxVkS7vU0kUR8SAlemY32g4RIjFhrbBELrGZPvffSWCuM'

access_token = '1347007868-f7fAQbPGAFpGfOeKlQCnmJMSZGdowk9pfC3BUhS'
access_token_secret = 'XpM39zQyWmSgb207W4kv2RVLwrCo04CVJLO5gZS3SXPM2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()
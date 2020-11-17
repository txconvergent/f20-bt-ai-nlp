import tweepy
import re
import json
import config
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

query = "UT Austin"
max_tweets = 3


def search_tweets(query, max_tweets):
    search_results = api.search(q=query, count=max_tweets, languages=["en"], tweet_mode="extended")

    for tweet in search_results:
        # regex to remove links
        text = re.sub(r"http\S+", '', tweet._json['full_text'], flags=re.MULTILINE)

        print(tweet._json['user']['name'] + " (@" + tweet._json['user']['screen_name'] + 
            "): " + text)
        print("--------------------------------------------------------")

def get_user_tweets(user, max_tweets):
    search_results = api.user_timeline(screen_name=user, count=max_tweets, languages=["en"], tweet_mode="extended")
    x = -1
    for tweet in search_results:
        # regex to remove links
        text = re.sub(r"http\S+", '', tweet._json['full_text'], flags=re.MULTILINE)
        #print(tweet)
        user_data = {
            u'name': tweet._json['user']['name'],
            u'tag':  '@' +  tweet._json['user']['screen_name'],
            u'tweet_text': text
        }
        db.collection(u'Tweets').document(u'UserTweets').collection(u'TheDailyTexan').add(user_data)
       
        print(tweet._json['user']['name'] + " (@" + tweet._json['user']['screen_name'] + 
            "): " + text)
        print("--------------------------------------------------------")
        if x<0:
            print(tweet._json)
            x += 1
    

def get_trends(lat=30.284477, lon=-97.736939):
    # get the trends location closest to the latitude, longitude coordinates
    closest_loc = api.trends_closest(lat, lon)
    trends = api.trends_place(closest_loc[0]['woeid'])

    for trend in trends[0]['trends']:
        print(trend['name'])

if __name__ == '__main__':
    get_user_tweets("thedailytexan", 10)
    search_tweets("UT Austin", 10)
    #get_trends()
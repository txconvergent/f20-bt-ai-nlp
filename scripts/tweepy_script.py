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
firebase_admin.initialize_app(cred, name = 'tweepy_script')
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
        # only sends to db if the post has more than 3 likes, weeds out dumb tweets
        if tweet._json['favorite_count'] > 10 :

            if "], 'urls': [{'url'" in tweet._json:
                # if tweet does contain a link
                tweet_with_link(tweet, text, u'TweetsOnCampus')
            else:
                # else if tweet does not have a link
                tweet_without_link(tweet, text, u'TweetsOnCampus')

        print("--------------------------------------------------------")
    print('###############################################################')

def get_user_tweets(user, max_tweets):
    search_results = api.user_timeline(screen_name=user, count=max_tweets, languages=["en"], tweet_mode="extended")
    x = -1
    for tweet in search_results:
        # regex to remove links
        text = re.sub(r"http\S+", '', tweet._json['full_text'], flags=re.MULTILINE)

        # only sends tweet to db if it isn't a retweet
        if text[:2] != 'RT':
            if "], 'urls': [{'url'" in tweet._json:
                # if tweet does contain a link
                tweet_with_link(tweet, text, u'UserTweets') 
            else:
                # else if tweet does not have a link
                tweet_without_link(tweet, text, u'UserTweets')
            '''
            if x<0:
                print(tweet._json)
                x += 1
            '''
        print("--------------------------------------------------------")
    print('###############################################################')




# adds tweet with a link to the db
def tweet_with_link(tweet, text, document):
    print(tweet._json['user']['name'] + " (@" + tweet._json['user']['screen_name'] + 
                "): " + text + tweet._json['entities']['urls'][0]['url'] + 'likes' + tweet._json['favorite_count']
                + 'link of the tweet:' 
                + 'https://twitter.com/{}/status/{}'.format(tweet._json['user']['screen_name'], tweet._json['id'])
                + 'date: ' + tweet._json['created_at'])
                
    user_data = {
        u'date': tweet._json['created_at'],
        u'name': tweet._json['user']['name'],
        u'tag': '@' +  tweet._json['user']['screen_name'],
        u'text': text,
        u'link_embedded_in_tweet': tweet._json['entities']['urls'][0]['url'],
        u'link_of_tweet': 'https://twitter.com/{}/status/{}'.format(tweet._json['user']['screen_name'], tweet._json['id'])
    }
    db.collection(u'Tweets').document(document).collection(u'{}'.format(tweet._json['user']['screen_name'])).add(user_data)

# adds tweet without a link to the db
def tweet_without_link(tweet, text, document):
    print(tweet._json['user']['name'] + " (@" + tweet._json['user']['screen_name'] + 
        "): " + text + '   link of tweet: ' + 'https://twitter.com/{}/status/{}'.format(tweet._json['user']['screen_name'], tweet._json['id'])
        + ' date: ' + tweet._json['created_at'])
    user_data = {
        u'date': tweet._json['created_at'],
        u'name': tweet._json['user']['name'],
        u'tag': '@' +  tweet._json['user']['screen_name'],
        u'text': text,
        u'link_of_tweet': 'https://twitter.com/{}/status/{}'.format(tweet._json['user']['screen_name'], tweet._json['id'])
    }
    db.collection(u'Tweets').document(document).collection(u'{}'.format(tweet._json['user']['screen_name'])).add(user_data)
   


def get_trends(lat=30.284477, lon=-97.736939):
    # get the trends location closest to the latitude, longitude coordinates
    closest_loc = api.trends_closest(lat, lon)
    trends = api.trends_place(closest_loc[0]['woeid'])

    for trend in trends[0]['trends']:
        print(trend['name'])

if __name__ == '__main__':
    get_user_tweets("UTAustin", 4)
    get_user_tweets("thedailytexan", 4)
    get_user_tweets('Healthyhorns', 4)
    get_user_tweets('TexasLonghorns', 4)
    search_tweets("UT Austin", 50)
    search_tweets("University of Texas at Austin", 50)
    # get_trends()
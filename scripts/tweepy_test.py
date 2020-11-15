import tweepy
import re
import json
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

query = "UT Austin"
max_tweets = 10


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

    for tweet in search_results:
        # regex to remove links
        text = re.sub(r"http\S+", '', tweet._json['full_text'], flags=re.MULTILINE)
        
        print(tweet._json['user']['name'] + " (@" + tweet._json['user']['screen_name'] + 
            "): " + text)
        print("--------------------------------------------------------")

def get_trends(lat=30.284477, lon=-97.736939):
    # get the trends location closest to the latitude, longitude coordinates
    closest_loc = api.trends_closest(lat, lon)
    trends = api.trends_place(closest_loc[0]['woeid'])

    for trend in trends[0]['trends']:
        print(trend['name'])

if __name__ == '__main__':
    #get_user_tweets("thedailytexan", 10)
    #search_tweets("UT Austin", 10)
    get_trends()
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
# is default firebase app as it is initialized first
firebase_admin.initialize_app(cred)
firebase_admin.initialize_app(cred, name = 'fastApi')
db = firestore.client()

# Import local scripts AFTER intializing firebase app
import NLP_summarizer
import UT_news_scraper
import daily_texan_scraper
import hornslink_scrapper
import tweepy_script

from fastapi import FastAPI
app = FastAPI()

# NOTE: THIS FORMAT CAN TAKE ANY OTHER NEWS SITE IN THE FUTURE
@app.get('/UTnews')
def get_UT_news():
    # run scripts to scrape daily texan and summarize article
    UT_news_scraper.main()
    NLP_summarizer.summarizeUTNews()

    db_data = db.collection(u'UTNews').document(u'Documents').collection(u'Summarized').get()
    data = []

    for doc in db_data:
        doc_data = {
            # TODO: CHANGE WHEN UPDATE MADE IN NLP_SUMMARIZER
            #'category': doc.get('category'),
            'title': doc.get('title'),
            'summary': doc.get('text'),
            'url': doc.get('url')
        }
        # Appends every doc in collection db_data to the list data
        data.append(doc_data)

    # data is added to the json file, which is ultimately returned
    with open(r'data\UT_news_data.json', 'w', encoding='utf-8') as f:
        # clears json and replaces with data list
        json.dump(data, f, indent = 6, ensure_ascii=False)
        UT_news_data = json.load(f)

    return UT_news_data

@app.get('/DailyTexan')
def get_UT_news():
    # run scripts to scrape daily texan and summarize article
    daily_texan_scraper.main()
    NLP_summarizer.summarizeDailyTexan()

    db_data = db.collection(u'DailyTexan').document(u'Documents').collection(u'Summarized').get()
    data = []

    for doc in db_data:
        doc_data = {
            # TODO: CHANGE WHEN UPDATE MADE IN NLP_SUMMARIZER
            #'category': doc.get('category'),
            'title': doc.get('title'),
            'summary': doc.get('text'),
            'url': doc.get('url')
        }
        # Appends every doc in collection db_data to the list data
        data.append(doc_data)

    # data is added to the json file, which is ultimately returned
    with open(r'data\daily_texan_data.json', 'w', encoding='utf-8') as f:
        # clears json and replaces with data list
        json.dump(data, f, indent = 6, ensure_ascii=False)
        UT_news_data = json.load(f)

    return UT_news_data


@app.get('/Tweets/{user_name}')
def get_user_tweets(user_name : str):
    # TODO: WE NEED TO TAKE DUPLICATE TWEETS INTO ACCOUNT
    tweepy_script.main()
    db_data = db.collection(u'Tweets').document(u'userTweets').collection(u'{}'.format(user_name)).get()
    data = []

    for doc in db_data:
        doc_data = {
            'username': doc.get('name'),
            'tag': doc.get('tag'),
            'date': doc.get('date'),
            'text': doc.get('text'),
            'tweet_link': doc.get('link_of_tweet'),
        }
        # Appends every doc in collection db_data to the list data
        data.append(doc_data)

    # data is added to the json file, which is ultimately returned
    with open(r'data\twitter_data.json', 'w', encoding='utf-8') as f:
        # clears json and replaces with data list
        json.dump(data, f, indent = 6, ensure_ascii=False)
        twitter_data = json.load(f)
        
        
            
    return twitter_data

@app.get('/Tweets/TweetsOnCampus')
def get_tweets_on_campus():
    tweepy_script.main()
    db_data = db.collection(u'Tweets').document(u'TweetsOnCampus').get()
    data = []

    for doc in db_data:
        tweet = doc.get()
        doc_data = {
            'username': doc.get('name'),
            'tag': doc.get('tag'),
            'date': doc.get('date'),
            'text': doc.get('text'),
            'tweet_link': doc.get('link_of_tweet'),
        }
        # Appends every doc in collection db_data to the list data
        data.append(doc_data)

    # data is added to the json file, which is ultimately returned
    with open(r'data\twitter_on_campus_tweets_data.json', 'w', encoding='utf-8') as f:
        # clears json and replaces with data list
        json.dump(data, f, indent = 6, ensure_ascii=False)
        twitter_on_campus_tweets_data = json.load(f)
        
            
    return twitter_on_campus_tweets_data

@app.get('/Hornslink')
def get_hornslink():
    hornslink_scrapper.main()
    db_data = db.collection(u'Hornslink').get()
    data = []

    for doc in db_data:
        doc_data = {
            'title': doc.get('title'),
            'date_and_time': doc.get('date_and_time'),
            'description': doc.get('description'),
            'host': doc.get('host'),
            'location': doc.get('location'),
            'url': doc.get('url')
        }
        # Appends every doc in collection db_data to the list data
        data.append(doc_data)

    # data is added to the json file, which is ultimately returned
    with open(r'data\hornslink_data.json', 'w', encoding='utf-8') as f:
        # clears json and replaces with data list
        json.dump(data, f, indent = 6, ensure_ascii=False)
        hornslink_data = json.load(f)
            
    return hornslink_data

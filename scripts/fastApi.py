from fastapi import FastApi
import NLP_summarizer
import UT_news_scraper
import hornslink_scrapper
import json
import tweepy_script
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastApi()

# NOTE: THIS FORMAT CAN TAKE ANY OTHER NEWS SITE IN THE FUTURE
@app.get('/UTnews')
def get_UT_news():
    UT_news_scraper.main()
    NLP_summarizer.main()
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
        json.dump(data, f, indent = 6, ensure_ascii=False)
        UT_news_data = json.load(f)
        # TODO: FIND A WAY TO CLEAR THE JSON FILE AFTER EVERY API CALL


    return UT_news_data


# MAKE IT SO THAT THE USER NAME PUT IN IS CALLED
@app.get('/Tweets/{SOME USER}')
def get_tweets():
    tweepy_script.main()
    db_data = db.collection(u'Tweets').document(u'userTweets').collection(u'SOME USER').get()
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
        json.dump(data, f, indent = 6, ensure_ascii=False)
        twitter_data = json.load(f)
        # TODO: FIND A WAY TO CLEAR THE JSON FILE AFTER EVERY API CALL
            
    return twitter_data

import config
import asyncio
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
from summarizer import Summarizer
from newspaper import fulltext
import requests


cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# get all data from the unsummarized collection in db  

def main():
    summarizeDailyTexan()
    summarizeUTNews()

if __name__ == "__main__":
    main()


def summarizeUTNews():
    all_data = db.collection(u'UTNews').document(u'Documents').collection(u'Unsummarized').get()
    # take text for each article, summarize it and add it to summarized collection
    #print('next is ', next(all_data))
    model = Summarizer()
    # TODO: REMEMBER TO CHANGE THE RANGE BELOW
    for doc in all_data[:4]:
        # gets raw, unsummarized article
        article =  doc.get('text')
        # summarizes the articles into 2 sentences
        result = model(article, num_sentences = 2)
        summary = "".join(result)
        new_data = {
            'text': summary,
            'title': doc.get('title'),
            'url': doc.get('url')
        }
        db.collection(u'UTNews').document(u'Documents').collection(u'Summarized').add(new_data)
        print('----------finished--------')

summarizeUTNews()

# take text for each article, summarize it and add it to summarized collection
def summarizeDailyTexan():
    all_data = db.collection(u'DailyTexan').document(u'Documents').collection(u'Unsummarized').get()

    model = Summarizer()
    # TODO: REMEMBER TO CHANGE THE RANGE BELOW
    for doc in all_data[:4]:
        # uses newpaper library to get text of article from the URL
        article = fulltext(requests.get(doc.get('URL')).text)
        # summarizes the articles into 2 sentences
        result = model(article, num_sentences = 2)
        summary = "".join(result)
        new_data = {
            'title': doc.get('title'),
            'url': doc.get('URL'),
            'text': summary,
            'genre': doc.get('genre')
        }
        db.collection(u'DailyTexan').document(u'Documents').collection(u'Summarized').add(new_data)
        print('----------finished--------')

summarizeUTNews()


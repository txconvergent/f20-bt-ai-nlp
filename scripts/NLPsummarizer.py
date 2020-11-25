import config
import asyncio
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
from summarizer import Summarizer


cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# get all data from the unsummarized collection in db  

def summarizeText():
    all_data = db.collection(u'UTNews').document(u'Documents').collection(u'Unsummarized').get()
    # take text for each article, summarize it and add it to summarized collection
    #print('next is ', next(all_data))
    model = Summarizer()
    for doc in all_data[:4]:
        article =  doc.get('text')
        result = model(article, num_sentences = 2)
        summary = "".join(result)
        new_data = {
            'text': summary,
            'title': doc.get('title'),
            'url': doc.get('url')
        }
        db.collection(u'UTNews').document(u'Documents').collection(u'Summarized').add(new_data)
        print('----------finished--------')

summarizeText()


'''
from newspaper import fulltext
import requests
article_url="https://thedailytexan.com/2020/11/09/ut-austin-student-government-petition-pass-fail"
article = fulltext(requests.get(article_url).text)
print(article)
'''

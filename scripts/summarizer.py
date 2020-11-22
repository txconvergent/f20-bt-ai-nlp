import config
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
all_data = 0
async def getCollection(data):
    all_data = db.collection(u'UTNews').document(u'Document').collection(u'Unsummarized')

# take text for each article, summarize it and add it to summarized collection
model = Summarizer()

for doc in allData:
    article = doc.get('text')
    result = model(article, num_sentences = 4)
    summary = "".join(result)
    new_data = {
        'text': summary,
        'title': doc.get('title'),
        'url': doc.get('url')
    }
    db.collection(u'UTNews').document(u'Document').collection(u'Summarized').add(new_data)


'''
from newspaper import fulltext
import requests
article_url="https://thedailytexan.com/2020/11/09/ut-austin-student-government-petition-pass-fail"
article = fulltext(requests.get(article_url).text)
print(article)
'''

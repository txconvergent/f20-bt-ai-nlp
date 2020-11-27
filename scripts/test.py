import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

db_data = db.collection(u'UTNews').document(u'Documents').collection(u'Summarized').get()
data = []

for doc in db_data:
    doc_data = {
        #'category': doc.get('category'),
        'title': doc.get('title'),
        'summary': doc.get('text'),
        'url': doc.get('url')
    }

    data.append(doc_data)

with open(r'data\UT_news_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent = 6, ensure_ascii=False)

#     out_file = open(r'data\UT_news_data.json', 'w')
#     data = out_file + doc_data
#     #json.dump(doc_data, out_file, indent = 6)

#     with open(r'data\UT_news_data.json', 'w', encoding='utf-8') as f:
#        f.write(json.dumps(doc_data, f, ensure_ascii=False))

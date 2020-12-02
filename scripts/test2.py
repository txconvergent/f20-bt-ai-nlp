
from newspaper import Article 
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
from newspaper import Article 

#link to firebase
cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

url = 'https://thedailytexan.com/2020/11/22/city-of-austin-expands-rent-assistance-program-allows-residents-6-months-rent-coverage'
article = Article(url, language = 'en')
article.download() 
article.parse() 

db.collection(u'DailyTexan').document(u'Documents').collection(u'Unsummarized').add({
    u'title': article.title,
    u'text': article.text,
    u'URL': url,
})
print('-----UPLOADED-----')
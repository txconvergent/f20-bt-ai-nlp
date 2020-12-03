import config
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
from summarizer import Summarizer
from newspaper import fulltext


cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
# TODO: FIGURE OUT THE FIREBASE APP THING
#firebase_admin.initialize_app(cred)
firebase_admin.initialize_app(cred, name = 'Summarizer')
db = firestore.client()

# get all data from the unsummarized collection in db  

def summarizeUTNews():
    print('UT NEWS SUMMARIZER START')
    all_data = db.collection(u'UTNews').document(u'Documents').collection(u'Unsummarized').get()
    # take text for each article, summarize it and add it to summarized collection
    #print('next is ', next(all_data))
    model = Summarizer()
    # TODO: REMEMBER TO CHANGE THE RANGE BELOW
    for doc in all_data[:]:
        # gets raw, unsummarized article
        article =  doc.get('text')
        # summarizes the articles into 2 sentences
        result = model(article, num_sentences = 1)
        summary = "".join(result)
        summary = u'{}'.format(summary)
        new_data = {
            # TODO: ONCE WORKING, DELETE ALL SUMMARIZED ARTICLES AND RESTART IT INCLUDING CATEGORY FIELD
            'category': doc.get('category'),
            'title': doc.get('title'),
            'text': summary,
            'url': doc.get('url')
        }
        db.collection(u'UTNews').document(u'Documents').collection(u'Summarized').add(new_data)
        print('----------finished--------')

    print('END')

# take text for each article, summarize it and add it to summarized collection
# NOTE: given just the title and URL, we can summarize articles for any other publication in 
#       future
def summarizeDailyTexan():
    all_data = db.collection(u'DailyTexan').document(u'Documents').collection(u'Unsummarized').get()

    model = Summarizer()
    for doc in all_data[:3]:
        # summarizes the articles into 2 sentences
        result = model(doc.get('text'), num_sentences = 1)
        summary = "".join(result)
        new_data = {
            'title': doc.get('title'),
            'url': doc.get('URL'),
            'text': summary,
        }
        db.collection(u'DailyTexan').document(u'Documents').collection(u'Summarized').add(new_data)
    

def main():
    #summarizeDailyTexan()
    summarizeUTNews()

if __name__ == "__main__":
    main()



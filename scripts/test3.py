
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
# is default app
firebase_admin.initialize_app(cred)
firebase_admin.initialize_app(cred, name = 'test3')
db = firestore.client()

import UT_news_scraper
import NLP_summarizer


def main():
    UT_news_scraper.main()
    NLP_summarizer.summarizeUTNews()

if __name__ == "__main__":
    main()
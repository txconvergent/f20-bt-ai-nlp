import requests
from bs4 import BeautifulSoup

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from newspaper import Article 

#link to firebase
cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#object connecting URL to the news category
class URLS(object):
    def __init__(self, url, category):
        self.url = url
        self.category = category

#object connecting the URL, category, title and article
class Event(object):
    def __init__(self, URLS, title, text):
        self.URLS = URLS
        self.title = title
        self.text = text

#scraping the news site for the URLs and its categories
def get_links():
    url = "https://news.utexas.edu/archive/"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    content = soup.find('section', {'class': 'content-wrapper'})

    url_list = []
    URLS_list = []

    for news in content.find_all('a'):
        try:
            if news.get('href') not in url_list and news.get('href').find("news.utexas.edu") == 8:
                if news.get('href').find("/archive/") == -1:
                    url_list.append(news.get('href'))
                    URLS_list.append(URLS(news.get('href'), "News"))
        except AttributeError:
            continue

    url = "https://news.utexas.edu/tag/covid-19/"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    content = soup.find('section', {'class': 'content-wrapper'})

    for news in content.find_all('a'):
        try:
            if news.get('href') not in url_list and news.get('href').find("news.utexas.edu") == 8:
                if news.get('href').find("/covid-19/") == -1:
                    url_list.append(news.get('href'))
                    URLS_list.append(URLS(news.get('href'), "Covid-19"))
        except AttributeError:
            continue

    url = "https://news.utexas.edu/campus-community/"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    content = soup.find('section', {'class': 'content-wrapper'})

    for news in content.find_all('a'):
        try:
            if news.get('href') not in url_list and news.get('href').find("news.utexas.edu") == 8:
                if news.get('href').find("/campus-community/") == -1:
                    url_list.append(news.get('href'))
                    URLS_list.append(URLS(news.get('href'), "Campus and Community"))
        except AttributeError:
            continue

    return URLS_list



# ALL I NEED IS THE LINKS 
def upload_to_db(links):
    for link in links:
        article = Article(link, language = 'en')
        article.download() 
        article.parse() 
        db.collection(u'DailyTexan').document(u'Documents').collection(u'Unsummarized').add({
            u'title': article.title,
            u'text': article.text,
            u'URL': link,
        })


#putting each article into the database
def main():
    upload_to_db()


if __name__ == "__main__":
    main()

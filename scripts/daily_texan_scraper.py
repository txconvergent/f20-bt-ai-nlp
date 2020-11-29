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

#scraping the news site for the URLs and its categories
def get_links():
    def get_links():
    url = "https://thedailytexan.com/section/news"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')

    url_list = []
    URLS_list = []

    for news in soup.find_all('div', {'class': 'story-image'}):
        try:
            news = news.find('a')
            if news.get('href') not in url_list:
                url_list.append(news.get('href'))
                URLS_list.append(URLS('https://thedailytexan.com' + news.get('href'), "News"))
        except AttributeError:
            continue

    url = "https://thedailytexan.com/section/campus"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')

    for news in soup.find_all('div', {'class': 'story-image'}):
        try:
            news = news.find('a')
            if news.get('href') not in url_list:
                url_list.append(news.get('href'))
                URLS_list.append(URLS('https://thedailytexan.com' + news.get('href'), "Campus"))
        except AttributeError:
            continue

    url = "https://thedailytexan.com/section/crime"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')

    for news in soup.find_all('div', {'class': 'story-image'}):
        try:
            news = news.find('a')
            if news.get('href') not in url_list:
                url_list.append(news.get('href'))
                URLS_list.append(URLS('https://thedailytexan.com' + news.get('href'), "Crime"))
        except AttributeError:
            continue

    url = "https://thedailytexan.com/section/university"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')

    for news in soup.find_all('div', {'class': 'story-image'}):
        try:
            news = news.find('a')
            if news.get('href') not in url_list:
                url_list.append(news.get('href'))
                URLS_list.append(URLS('https://thedailytexan.com' + news.get('href'), "University"))
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

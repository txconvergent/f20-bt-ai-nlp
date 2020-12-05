import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from newspaper import Article

# links to firebase
cred = credentials.Certificate(
    r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred, name='daily_texan_scraper')

db = firestore.client()

# stores a articles URL and category
class URLS(object):
    def __init__(self, url, category):
        self.url = url
        self.category = category

    def get_url():
        return object.url


# Gets link of the latest articles from the relevant categories in the DailyTexan, ignores
# repeats
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
                URLS_list.append(
                    URLS('https://thedailytexan.com' + news.get('href'), "News"))
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
                URLS_list.append(
                    URLS('https://thedailytexan.com' + news.get('href'), "Campus"))
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
                URLS_list.append(
                    URLS('https://thedailytexan.com' + news.get('href'), "Crime"))
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
                URLS_list.append(
                    URLS('https://thedailytexan.com' + news.get('href'), "University"))
        except AttributeError:
            continue

    return URLS_list


# Given just the links to a article from any publication, this code can extract all needed
# data and upload to respective Firebase collection
def upload_to_db(links):
    for link in links:
        # Article() is part of the newspaper3k library, automatically scrapes article
        article = Article(link, language='en')
        article.download()
        article.parse()
        db.collection(u'DailyTexan').document(u'Documents').collection(u'Unsummarized').add({
            u'title': article.title,
            u'text': article.text,
            u'URL': link,
        })


def main():
    links = []
    # gets article links
    all_links = get_links()
    for i in range(0, len(all_links)):
        link = all_links[i].url
        links.append(link)
    # scrapes and uploads to Firebase
    upload_to_db(links)


if __name__ == "__main__":
    main()

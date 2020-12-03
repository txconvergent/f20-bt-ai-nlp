import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from newspaper import Article

# link to firebase
cred = credentials.Certificate(
    r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred, name='daily_texan_scraper')

db = firestore.client()

# object connecting URL to the news category


class URLS(object):
    def __init__(self, url, category):
        self.url = url
        self.category = category

    def get_url():
        return object.url

# scraping the news site for the URLs and its categories


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

# ALL I NEED IS THE LINKS


def upload_to_db(links):
    for link in links:
        article = Article(link, language='en')
        article.download()
        article.parse()

        db.collection(u'DailyTexan').document(u'Documents').collection(u'Unsummarized').add({
            u'title': article.title,
            u'text': article.text,
            u'URL': link,
        })
        print('----UPLOADED--------')


# putting each article into the database
def main():
    links = []
    all_links = get_links()
    for i in range(0, len(all_links)):
        link = all_links[i].url
        links.append(link)
    links = ['https://thedailytexan.com/2020/11/29/New-online-dashboard-estimates-COVID-19-risks-for-schools-across-country', 'https://thedailytexan.com/2020/11/22/4-of-5-leading-covid-19-vaccine-candidates-use-ut-research', 'https://thedailytexan.com/2020/11/17/US-Department-of-Energy-invests-4.1-million-for-UT-Austins-Petawatt-Laser', 'https://thedailytexan.com/2020/11/17/ut-expands-window-to-apply-for-extension-of-stay-for-international-students', 'https://thedailytexan.com/2020/11/13/ut-austin-administrators-discuss-passfail-policies-covid-19-safety-at-ut-senate-town-hall',
             'https://thedailytexan.com/2020/11/12/texas-advance-commitment-expansion-brings-tuition-help-confusion-to-ut-austin-students', 'https://thedailytexan.com/2020/11/12/ut-austin-chemical-engineering-professor-fired-sexual-misconduct-adam-heller', 'https://thedailytexan.com/2020/11/09/the-eyes-of-texas-university-committee', 'https://thedailytexan.com/2020/11/08/Prevalent-mutation-may-cause-COVID-19-to-be-more-contagious-likely-wont-hinder-vaccine-efficacy']
    upload_to_db(links)


if __name__ == "__main__":
    main()

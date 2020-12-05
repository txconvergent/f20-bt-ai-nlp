from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"C:\Users\akifa\OneDrive\Documents\GitHub\f20-bt-ai-nlp\scripts\forestoreKey.json")
firebase_admin.initialize_app(cred, name = 'hornslink_scraper')

db = firestore.client()


#event object, just makes storing and reading the data for the events easier
class Event(object):

    def __init__(self, url, title, date_and_time, location, description, host = None,):

        self.url = url
        self.title = title
        self.date_and_time = date_and_time
        self.location = location
        self.host = host
        self.description = description
    
    def __str__(self):

        print('Url: ', self.url)
        print('Title: ', self.title)
        print('Host: ', self.host)
        print('Date and Time: ', self.date_and_time)
        print('Location: ', self.location)
        print('Description: ', self.description)
        
        return ""

#this function gets the URLS to each event from the hornslink events page
def get_event_links():

    #headless browser stuff
    options = webdriver.FirefoxOptions()
    options.headless = True

    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = options)
    url = 'https://utexas.campuslabs.com/engage/events'
    browser.get(url)
    time.sleep(5)
    html = browser.page_source
    browser.close()

    soup = BeautifulSoup(html, features = 'html.parser')

    #the div where the urls are located
    event_list = soup.find('div', {'id': 'event-discovery-list'})

    link_list = []

    for a in event_list.find_all('a', href = True):
        link_list.append('https://utexas.campuslabs.com' + a['href'])

    return link_list

#this function visits every link from the main events page and collects the data from those pages
def get_info():

    link_list = get_event_links()

    event_list = []

    #can set it to run for all the links, but that takes a lot of time so I made it to where you can adjust
    #how many events you want to see by just uncommenting the two lines below and commenting 
    #the for link in link_list: in case you are testing
    for link in link_list:
    #for i in range(3):
    
        #link = link_list[i]

        #more browser stuff
        options = webdriver.FirefoxOptions()
        options.headless = True

        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = options)
        browser.get(link)
        time.sleep(5)
        html = browser.page_source
        browser.close()

        soup = BeautifulSoup(html, features = 'html.parser')

        #this is where the title is ocated
        for h1 in soup.find_all('h1'):
            title = h1.text.strip()

        #tries to find host
        #### KNOWN BUG #### 
        #sometimes the host and description get switched or messed up, has to do with how the 'host' data is found
        #might even strip the host data all together if the issue persists
        try:
            h3 =  soup.find_all('h3')
            host = h3[0].text.strip()
        except IndexError:
            host = None
            print('No Host')
        
        #grabs all the text in the <p> elements
        text_list = []
        for p in soup.find_all('p'):
            text_list.append(p.text.strip())

        #they retain the same order for each link so simple to grab the following information
        date_and_time = text_list[0][:-3] + 'to ' + text_list[1]
        location = text_list[2]
        description = text_list[3]

        #appends a list with the new event
        event_list.append(Event(link, title, date_and_time, location, description, host))
    
    return event_list


def main():

    events = get_info()

    #goes through each event and adds it to firebase as well as printing it to the console.
    for event in events:
        doc_ref = db.collection(u'Hornslink')
        doc_ref.add({
            u'url': event.url,
            u'title': event.title,
            u'host': event.host,
            u'date_and_time': event.date_and_time,
            u'location': event.location,
            u'description': event.description
        })
        print(event)
        print()


if __name__ == "__main__":
    main()
# UTrends
## f20-bt-ai-nlp

[Logo](https://drive.google.com/file/d/1XhUxQwym5rZwr8NbGql3SqGvKSVTTm9X/view?usp=sharing)
[Presentation](https://docs.google.com/presentation/d/1GM5yk99FoLEdQrvWQrXttu1FRn96uA_L5eFhwBGK6lk/edit?usp=sharing)

UTrends is a project for the Texas Convergent AI NLP build team for the Fall of 2020.

Python tech stack used -
* React Native
* Firebase
* FastAPI

**Walking through the app code** -

<h2>BACKEND</h2>
The app depends on several python scraper scripts to collect needed data from news sites, social media, etc. So far, we have scrapers for Twitter, The Daily Texan, UT News, and Hornslink, __however__, since we have a established script skeleton that is adabtable to any news site and social media account, it is very easy to add more sources of data for our app. 

***News scraper***: Once we have a list of article links, the newspaper3k python library allows us to effortlessly parse and scrape through any article in any news site, therefore eliminating the need for us to make customized scrapers for every news publication. Look at daily_texan_scraper.py for example.
 
To summarize article texts, which tend to hover around a word count of 400-700, we use the BERT summarizer - a Natural Language Processor model developed by Google. The summarizer whittles down articles to 50-120 words, which is ultimately what is shown in the app. Look at NLP_summarizer.py for more.

***Twitter***: We utilized the Tweepy API to store both "trending" tweets around the UT Austin campus and specific accounts, such as @TexasFootball and @UTAustin. Look at tweepy_scraper.py for more.

***FastAPI***: FastAPI is a efficient, quick Python backend framework, we used FastAPI because of its ease of use and capability. Look at fastApi.py for more.

<h2>FRONTEND</h2>
We utlized React Native to create the backend of the program.



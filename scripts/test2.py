
from newspaper import Article 

url = 'https://thedailytexan.com/2020/11/22/city-of-austin-expands-rent-assistance-program-allows-residents-6-months-rent-coverage'
article = Article(url, language = 'en')
article.download() 
article.parse() 
article.nlp() 
print('Article title: ', article.title)

print('Article text: ', article.text)
print("Article's Summary:") 
print(article.summary) 

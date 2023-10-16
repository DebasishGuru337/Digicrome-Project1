#Task 1: Web Scraping: Use libraries like requests and BeautifulSoup to scrape data from a website [Welcome to Python. org]
import requests
from bs4 import BeautifulSoup
from collections import Counter
url="https://www.python.org/"
def python_latest_articles():
    respose=requests.get(url)
    if respose.status_code==200:
        soup=BeautifulSoup(respose.text,'html.parser')
        latest_articles=[]
        for articles in soup.select(".blog-widget li"):
            title=articles.a.text.strip()
            latest_articles.append(title)
        return latest_articles
if __name__=='__main__':
    python_articles=python_latest_articles()
    if python_articles:
        print('latest articles in python section are :')
        for index,articles in enumerate(python_articles,1):
            print(f'{index} : {articles}')
#Task 2: Word Frequency Create a program that reads a created text file from task 1 and counts the frequency of each word.   
all_title=''.join(python_articles)
words=all_title.split()
word_count=Counter(words)
for word in words:
    #Removed the punctuation and convert to lowercase
    word=word.strip().lower()
    if word:
         word_count[word] +=1
# sort the words by decending order 
word_count=word_count.most_common()
for word,count in word_count:
        print(f'{word} : {count}')
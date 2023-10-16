#Task 1: Web Scraping: Use libraries like requests and BeautifulSoup to scrape data from a website [Welcome to Python. org]
import requests
from bs4 import BeautifulSoup
url='https://www.python.org/'
response=requests.get(url)
html=response.text
if response.status_code==200:
    soup=BeautifulSoup(html,'html.parser')
    title=soup.find('title')
    if title:
        print('title is :',title.text)
    else:
        print('title is not found ')

# Also we can Exttract the links.
links=soup.find_all('a')
for link in links:
    print('Links are :', link.get('href'))
else:
    print('Faild to retrive the code from the web pages',)
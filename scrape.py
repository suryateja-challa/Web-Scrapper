import requests
from bs4 import BeautifulSoup as bs

url = 'https://news.ycombinator.com/news'

links = []
website = requests.get(url)

soup = bs(website.text, features='html.parser')

for link in soup.find_all('a'):
    links.append(link.getText('href'))

for link in links:
    print(link)


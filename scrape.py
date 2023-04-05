import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://news.ycombinator.com/news')
soup = bs(response.text, 'html.parser')

print(soup.select('.titleline')[0])
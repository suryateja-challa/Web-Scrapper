import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://news.ycombinator.com/news')
print(response.status_code)
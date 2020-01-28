import requests
from bs4 import BeautifulSoup

url = 'https://inshorts.com/en/read'
html = requests.get(url)

if html.status_code == 200:
    BeautifulSoup.find_all("div", class_="block-image")

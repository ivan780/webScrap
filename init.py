import requests
from bs4 import BeautifulSoup

# realizamos la peticion a la web
url = 'https://computerhoy.com/'
html = requests.get(url)

# comprobamos que todo este bien por el codfigo de error
if html.status_code == 200:
    soup = BeautifulSoup(html.content, 'html.parser')
    div = soup.find_all("div", class_="block-title")
    title = div[0].find('a').getText()

    print(title)

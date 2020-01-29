import requests
from bs4 import BeautifulSoup


def createDiv(pSource, pTitle):
    text = """
    <picture>
            <img src="{}"  alt="test"/>
        </picture>
            <p>{}</p>
    """.format(pSource, pTitle)
    return text


# realizamos la peticion a la web
url = 'https://computerhoy.com/'
html = requests.get(url)

# comprobamos que todo este bien por el codfigo de error
if html.status_code == 200:
    soup = BeautifulSoup(html.content, 'html.parser')

    divTitle = soup.find_all("div", class_="block-title")
    title = divTitle[0].find('a').getText()
    divImage = soup.find_all("div", class_="block-image")
    image = divImage[0].find('img')
    body = createDiv(image['src'], title)

    title = divTitle[1].find('a').getText()
    image = divImage[1].find('img')
    body += createDiv(image['src'], title)

    title = divTitle[2].find('a').getText()
    image = divImage[2].find('img')
    body += createDiv(image['src'], title)

    f = open('titular.html', 'wb')
    start = """
    <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>
        """
    end = """
    </body>
    </html>
    """
    message = start + body + end
    f.write(message.encode())
    f.close()

else:  # Si nos devuelve otro codigo mostramos el error
    print("Error en la peticion, codigo de error: {}".format(html.status_code))

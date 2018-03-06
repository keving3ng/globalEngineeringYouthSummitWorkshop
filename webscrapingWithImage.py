from bs4 import BeautifulSoup
import urllib.request
import requests
from PIL import Image

link = "https://www.reddit.com/"

def webscraper():
    opensite = urllib.request.urlopen(link)
    site_content = opensite.read()
    soup = BeautifulSoup(site_content, "lxml")
    soup.prettify()
    posts = soup.select('div#siteTable div.thing')
    print(posts[0].select("p.title a")[0].text)
    print(posts[0].select("a.thumbnail img")[0].get("src"))

    image_name = "Image.jpg"
    img1 = posts[0].select("a.thumbnail img")[0].get("src")
    img1 = "http:" + img1
    TheImage = requests.get(img1)

    with open(image_name, "wb") as f:
        f.write(TheImage.content)


    image = Image.open(image_name)
    image.show()



webscraper()

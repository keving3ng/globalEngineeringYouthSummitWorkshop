from bs4 import BeautifulSoup
import urllib.request
import requests
from PIL import Image
from io import BytesIO

link = 'https://old.reddit.com/'

def webscraper():
    opensite = urllib.request.urlopen(link)

    site_content = opensite.read()
    soup = BeautifulSoup(site_content, "lxml")
    soup.prettify()
    posts = soup.select('div#siteTable')
    print(posts[0].select("a.title.may-blank")[0].text)
    #same thing more specific
    print(posts[0].select("div.entry.unvoted div.top-matter p.title a")[0].text)

    #One way of getting an image and saving it to file then showing it
    image_name = "Image.jpg"
    img1 = "https:" + posts[0].select("a img")[0].get("src")
    # img1 = "https:" + img1
    TheImage = requests.get(img1)

    with open(image_name, "wb") as f:
        f.write(TheImage.content)

    image = Image.open(image_name)
    image.show()

    #Or just show the image and use some shortcuts to use less code.
    #getting the url for the route image
    href = posts[0].select("div")[0].get("data-url")
    #check the url
    print(href)
    #add the image and show it
    sample_image = Image.open(BytesIO(requests.get(href).content))
    sample_image.show()

    #another way to show an image



webscraper()

from bs4 import BeautifulSoup
import urllib.request

link = "https://old.reddit.com/"
def simple_webscraper(link):
    opened_link = urllib.request.urlopen(link)
    site_content = opened_link.read()
    soup = BeautifulSoup(site_content, "lxml")
    soup.prettify()
    posts = soup.select('div#siteTable div.thing')
    first_entry = posts[0]
    #so if we have <p class="title">
    #<a href="link if the post"> Title of the post</a>
    #then we know that what we need is to grab these things,
    #to get a link to the post we would use the href tag,
    #to get the text we can just use the .text tag.
    info1 = first_entry.select("p.title a")[0]
    title1 = info1.text
    print(title1)
simple_webscraper(link)

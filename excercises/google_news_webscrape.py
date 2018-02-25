from bs4 import BeautifulSoup
import requests
url = "https://news.google.com/news/rss"
page = requests.get(url).text

soup = BeautifulSoup(page,"xml")

headlines = soup.findAll("item")


for headline in headlines:
    print headline.title.text
    print headline.link.text
    print "=="*30
    print "\n"

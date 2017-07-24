# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#import the library used to query a website

import urllib3
import certifi
#http://urllib3.readthedocs.io/en/latest/user-guide.html#ssl

#https://urllib3.readthedocs.io/en/latest/
# instead of using urllib2 from this article I'm using urllib3
# specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# query the website and return the html to the variable 'page'
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

r = http.request('GET', wiki)
print(r.status)
print(r.data)

from bs4 import BeautifulSoup

# parse the html in the page variable and store it in beatuful soup format
soup = BeautifulSoup(r.data, "html.parser")

print(soup.prettify())
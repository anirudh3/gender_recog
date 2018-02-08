
import urllib2
from bs4 import BeautifulSoup

import re



# specify the url
data_page = "http://www.wavsource.com/people/men.htm"


hdrs = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(data_page, headers=hdrs)

# query the website and return the html to the variable 'page'
main_page = urllib2.urlopen(req)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(main_page, 'html.parser')



# print type(soup)

# getting the audio box area audio_box =

for tag in soup.find_all(href=re.compile("v$")):
    print tag



# soup.find

# print soup.prettify()

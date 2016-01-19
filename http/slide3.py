
from bs4 import BeautifulSoup
import urllib

url=raw_input('Enter url - ')

html=urllib.urlopen(url)
soup=BeautifulSoup(html,'lxml')

tags=soup('a')

print 'links start now'
for tag in tags:
    print tag.get('href',None)

print 'EOP'

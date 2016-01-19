
from bs4 import BeautifulSoup

import urllib

#get the numbers in a particular tag all and print the sum
#linktosearch='http://python-data.dr-chuck.net/comments_42.html'
linktosearch='http://python-data.dr-chuck.net/comments_228632.html'

mysoup=BeautifulSoup(urllib.urlopen(linktosearch))

tagtosearch=raw_input('print the tag to search for - ')

summer=0
counter=0
for tag in mysoup.find_all(tagtosearch):
    counter=counter+1
    summer=summer+int(tag.string)

print 'searched for - ',tagtosearch
print 'got entries in number - ',counter
print 'summing to - ',summer


import urllib
from bs4 import BeautifulSoup
import ssl
scontext=ssl.SSLContext(ssl.PROTOCOL_TLSv1)

#first get the html of the link and print to see what it gets
#linktosearch='https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
linktosearch='https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Xiong.html'

myhtml=urllib.urlopen(linktosearch,context=scontext)

'''myhtml_=myhtml.read()

print myhtml_'''

linknum=int(raw_input('Enter the link number to search for in each page - '))
whichpage=int(raw_input('Enter the page to stop the result at - '))

#function to get the tag in the link
def getnthlinktag(inplink,linkno):
    #change to http search
    #inplinkmod=inplink.replace('https://','http://')
    inplinkmod=inplink
    #open the url in to soup
    soup=BeautifulSoup(urllib.urlopen(inplinkmod,context=scontext))
    #get the tags
    alllinktags=soup.find_all('a')
    '''print 'from link ',inplink,' got '
    print alllinktags'''
    return alllinktags[linkno-1]

baselink=linktosearch
names=[]
for n in xrange(whichpage):
    mytag=getnthlinktag(baselink,linknum)
    baselink=mytag['href']
    names.append(mytag.string)

print names
print names[-1]

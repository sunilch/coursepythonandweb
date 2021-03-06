
import urllib
from bs4 import BeautifulSoup
import re

baselink='http://www.pythonlearn.com/code/'

#get the different types of files in the base link

soup=BeautifulSoup(urllib.urlopen(baselink),'lxml')

allextensions=[]

linktags=soup.find_all('a')

def getextension(inpurl):
    '''returns the extension of the file name pointed to by inpurl'''
    if inpurl==None:
        return None
    lastpart=inpurl.split('/')[-1]
    if '.' not in lastpart:
        return None
    ext=lastpart.split('.')[-1]
    return ext

for tag in linktags:
    myext=getextension(tag.get('href',None))
    if myext not in allextensions and myext!=None:
        allextensions.append(myext)

print 'different extensions are '+','.join(allextensions)

whichext=raw_input('Enter the type of extensions to be downloaded - ')
basedir=raw_input('Enter the base directory name - ')

exttags=soup.find_all('a',attrs={'href':re.compile('*\.'+whichext+'$')})

print exttags

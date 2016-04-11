
import urllib
from bs4 import BeautifulSoup
import re

baselink='http://www.pythonlearn.com/code/'
baselink='http://wallpapercave.com/surrealism-wallpaper'

#get the different types of files in the base link

soup=BeautifulSoup(urllib.urlopen(baselink),'lxml')

allextensions=[]

linktags=soup.find_all('a')

wallpapertags=soup.find_all('a',attrs={'class':'addtofavorite'})

dir='~/Documents/wallpapers/'
dir='/Users/schidara/Documents/wallpapers/'
for tag in wallpapertags:
    linkname=tag['src']
    print 'downloading',linkname
    fname=linkname.split('/')[-1]
    urllib.urlretrieve(linkname,dir+fname)

#tag['src']

import sys

import re

filename='regex_sum_228627.txt'

fo=open(filename)

sumall=0
for line in fo:
    mylist=[]
    mylist=re.findall('[0-9]+',line)
    print line
    print mylist
    for word in mylist:
        sumall=sumall+int(word)
        print word
print 'final sum is',sumall

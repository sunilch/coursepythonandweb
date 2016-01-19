
import sys
import re

myline='From: to when:'

#regextosearch='^F.+:'
regextosearch=sys.argv[1]

y=re.findall(regextosearch,myline)

print 'matches are',y

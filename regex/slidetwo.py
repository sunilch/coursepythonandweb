
import sys
import re

myline='My Favourite 2 numbers are 19 and 42'

#regextosearch='[0-9]+'
regextosearch=sys.argv[1]

y=re.findall(regextosearch,myline)

print 'matches are',y


import sys
import re

myline='From sunil.chidara@gmail.com 5 09:15'

#regextosearch='\S+@\S+'
regextosearch=sys.argv[1]

y=re.findall(regextosearch,myline)

print 'matches are',y

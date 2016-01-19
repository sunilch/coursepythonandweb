
import re
import sys

hand = open('../downloads/mbox-short.txt')

if not len(sys.argv)==2:
    print 'Please give only regex to search'

regextofind=sys.argv[1]

for line in hand:
    line=line.rstrip()
    if re.search(regextofind,line):
        print line

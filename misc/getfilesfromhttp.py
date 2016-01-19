
import sys, urllib, re, urlparse
from bs4 import BeautifulSoup

if not len(sys.argv) == 2:
    print >> sys.stderr, "Usage: %s <URL>" % (sys.argv[0],)
    sys.exit(1)

url = sys.argv[1]

f = urllib.urlopen(url)
soup = BeautifulSoup(f)
for i in soup.findAll('img', attrs={'src': re.compile('(?i)(txt|py)$')}):
    full_url = urlparse.urljoin(url, i['src'])
    print "image URL: ", full_url

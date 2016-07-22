import urllib.request
from bs4 import BeautifulSoup
import re
root_url = input('your url:')
request = urllib.request.Request(root_url)
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1)')
try:
    response = urllib.request.urlopen(request)
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)

soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
urllinks= set(soup.find_all('a',href=re.compile(r'/p/.*pn=')))
for link in urllinks:
   print(link['href'])
   print(type(link['href']))
##for url_ in urllinks['href']:
##    print(url_)


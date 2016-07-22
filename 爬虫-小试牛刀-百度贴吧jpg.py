import urllib.request
from bs4 import BeautifulSoup
import re
import os

location=input('your filename:')    
filename = os.mkdir('location')
os.chdir(os.path.join(os.getcwd(), filename))

root_url = input('your url:')
request = urllib.request.Request(root_url)
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1)')

def open_url()
        try:
        response = urllib.request.urlopen(request)
        except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)

soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
   


x=0                        
links =soup.find_all('img',class_='BDE_Image',src=re.compile(r"\.jpg"))
for link in links:
    src=link['src']
    try:
        
        print('正在下载第 %s张'%x)
        urllib.request.urlretrieve(src,'%s.jpg'%x)
    except:
        print('Fail to download'+ '%s.jpg'%x)
    x+=1


 


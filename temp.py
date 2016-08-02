import requests
from bs4 import BeautifulSoup
import re





    

    
    
def get_urls(url):
    global undo
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    r=requests.get(root_url, headers=headers)
    soup=BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
    links =soup.find_all('a',href=re.compile(r"\/search\/flip\?tn=baiduimage"))
    for link in links:
        url_find='http://image.baidu.com'+link['href']

    while len(undo)<=50:
        if url_find not in undo:
            print('new found url:','')
            print(url_find)
            undo.add(url_find)
            get_urls(url_find)
    return undo
if __name__=='__main__':
    undo=set()
    root_url='http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E9%A3%8E%E6%99%AF&ct=201326592&v=flip'

    undo=get_urls(root_url)
   
    for each in undo:
        print('all found urls:')
        print(each)
        

        
        
    
    

 

##print(imgurls)

                           
##print(r.status_code)
##for imgurl in imgurls:
##    url_total.append(imgurl)
##print(imgurl)
##print(r.text)
##print(r.content)

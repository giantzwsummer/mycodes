import requests
from bs4 import BeautifulSoup
import re
import time
#‘终于可以遍历百度图片传统版本，但是搜索算法比较低级，效率不高！’

   
def get_urls(root_url):
    global undo
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    r=requests.get(root_url, headers=headers)
    soup=BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
    links =soup.find_all('a',href=re.compile(r"\/search\/flip\?tn=baiduimage"))
    
    while len(undo)<15:

        for link in links:
            url_find='http://image.baidu.com'+link['href']
            strinfo = re.compile(r"\&gsm=.*")
            url_find =strinfo.sub('',url_find)
            
            if url_find not in undo:
               
                undo.add(url_find)
                time.sleep(1)
                get_urls(url_find)
        return undo

def main(keyword):
    
    
    root_url='http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+keyword+'&ct=201326592&v=flip'
    find=get_urls(root_url)
    print('all found urls:')
    for each in find:
        
        print(each)
    
    
    
if __name__=='__main__':
    keyword=input('what do you want：')
    undo=set()
    print('downing,inpurt "ctrl+c"to stop')
    main(keyword)

   
   

        
        
    
    

 



                           
##print(r.status_code)
##for imgurl in imgurls:
##    url_total.append(imgurl)
##print(imgurl)
##print(r.text)
##print(r.content)

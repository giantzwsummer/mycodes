import urllib.request
from bs4 import BeautifulSoup
import re
import os
import socket

# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)
# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module

#‘准备保存图片的文件夹'
location=input('where to store:')#'获得文件名'
location='e://python downloacd//'+location#'拼接path到指定目录'
os.makedirs(location)#'创建这个子目录'
os.chdir(location)#'切换到这个目录'


url_all=[]
url = input('your url:')
url_all.append(url)

#'定义下载url函数，防错机制'
def get_url(url):
        try:
                request = urllib.request.Request(url)
                request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1)')
                response = urllib.request.urlopen(request)
        except urllib.error.URLError as e:
                if hasattr(e,'code'):
                    print(e.code)
                if hasattr(e,'reason'):
                    print(e.reason)
                return None
        return response


#'定义图片下载函数'
def down_load(src,x):
            try:
                
                print('正在从地址'+a_url+'下载第 %s张'%x)
                urllib.request.urlretrieve(src,'%s%s.jpg'%(y,x))
            except:
                print('Fail to download'+ '%s.jpg'%x)
            x+=1
            
response=get_url(url)

#'解析获得除主url外其它页面url'
soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
urllinks= soup.find_all('a',href=re.compile(r'/p/\d+.pn=')) #'这步筛选没有直接取得剩余url，有重复url，有待优化'
if urllinks==None:
        print('only one page to scrapy')
else:
        #'补全url'
        for link in urllinks:

                linkurl='http://tieba.baidu.com'+link['href']
                url_all.append(linkurl)
        #'排序去重'
        print('the urls you wanted are blew:')
        urls=sorted(set(url_all))
        for each_url in urls:
                print(each_url)
        

   
y=0
total=[]#'创建列表，将每个页面下图片数量x加入列表，最后求和得出下载了多少图片'
for a_url in urls:
#'获得每个url中的图片下载地址,此处图片名称数量还有待优化'
        response_= get_url(a_url)
      
        soup = BeautifulSoup(response_,'html.parser',from_encoding='utf-8')
    
        links =soup.find_all('img',class_='BDE_Image',src=re.compile(r"\.jpg"))
##        print(links)
        
        x=0
        for link in links:
            src=link['src']
            down_load(src,x)
            x+=1
        y+=1

        total.append(x)

        
print('the number of pictures downloaded is %s:'%sum(total))

 


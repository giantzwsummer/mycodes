##Skip to content
##This repository
##Search
##Pull requests
##Issues
##Gist
## @giantzwsummer
## Unwatch 1
##  Star 0
##  Fork 0 giantzwsummer/mycodes
## Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs  Settings
##Branch: master Find file Copy pathmycodes/爬虫-小试牛刀-百度贴吧jpg.py
##6cc6478  3 days ago
##@giantzwsummer giantzwsummer Add files via upload
##1 contributor
##RawBlameHistory     85 lines (66 sloc)  2.57 KB
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import socket

timeout = 2
socket.setdefaulttimeout(timeout)

#‘准备保存图片的文件夹'
location=input('where to store:')#'获得文件名'
location='e:\\lyx\\python download\\'+location
if not os.path.exists(location):#'如果不存在，则创建并切换到这个目录'
    os.makedirs(location) 
    os.chdir(location)
else:  #'如果存在文件目录，覆盖输入1，放弃并结束程序输入0'
    print('the file is already existed')
    value=int(input('print "1" to go on,or "0"to exit '))
    if value:
        os.chdir(location)
        print("Let' go on")
    elif not value:
        print('bye-bye')
        os._exit(0)
    
    
        
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
#‘定义图片下载函数’
def down_load(src,x):
            try:
                
                print('正在从地址'+a_url+'下载第%d %d张'%(y,x))
                urllib.request.urlretrieve(src,'%d%d.jpg'%(y,x))
            except:
                print('Fail to download the'+a_url+ '%d%d.jpg'%(y,x))
            x+=1
            
response=get_url(url)
if response==None:
        print('error shuntdown')

#'解析获得除主url外其它页面url'
soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
urllinks= soup.find_all('a',href=re.compile(r'/p/\d+.pn=')) #'这步筛选没有直接取得剩余url，有重复url，有待优化'

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
        links =soup.find_all('a',src=re.compile(r"\.jpg"))#'需要修改'
        print(links)
##        if links==None:
##            print('no links at all')
##            os._exit(0)
        
        x=0
        for link in links:
            src=link['src']
            down_load(src,x)
            x+=1
        y+=1

        total.append(x)

        
print('the number of pictures downloaded is %s:'%sum(total))

 
##
##Contact GitHub API Training Shop Blog About
##© 2016 GitHub, Inc. Terms Privacy Security Status Help

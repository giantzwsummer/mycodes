import urllib.request
from bs4 import BeautifulSoup
import re
import os
import time
import socket
timeout = 2
socket.setdefaulttimeout(timeout)

#'定义寻找页面里所有待爬取img地址并下载，防错机制'
def get_img(url,x,name):
    try:
        request = urllib.request.Request(root_url)
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1)')
        response_ = urllib.request.urlopen(request)
        soup = BeautifulSoup(response_,'html.parser',from_encoding='utf-8')
        links =soup.find_all('img',class_='BDE_Image',src=re.compile(r"\.jpg"))
        for link in links:
            src=link['src']
            x=down_load(src,x,name)
            time.sleep(1)
        
        
    except urllib.error.URLError as e:
                if hasattr(e,'code'):
                    print(e.code)
                if hasattr(e,'reason'):
                    print(e.reason)
                return None
    return x
    

#'定义寻找所有待爬取url函数，防错机制'
def get_url(root_url):
        try:
                request = urllib.request.Request(root_url)
                request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1)')
                response = urllib.request.urlopen(request)
                #'解析获得除主url外其它页面url'
                soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
                urllinks= soup.find_all('a',src=re.compile(r'/p/\d+.pn='))#'这步筛选没有直接取得剩余url'
                #'补全url'
                url_all=[]
                for link in urllinks:
                   
                    linkurl='http://tieba.baidu.com'+link['href']#'字符替换，感觉比下面正则替换简单，但速度比较未知'
                ##   linkurl=re.sub(r'/p/\d+.pn=',link['href'],'http://tieba.baidu.com'+link['href'])
                    url_all.append(linkurl)
                #'排序去重'
                print('the urls you wanted are blew:')
                urls=sorted(set(url_all))#'去重排序'
                for each_url in urls :
                    print(each_url)#'打印所有要爬取的url'
                return urls
                       
        except urllib.error.URLError as e:
                if hasattr(e,'code'):
                    print(e.code)
                if hasattr(e,'reason'):
                    print(e.reason)
                return None
            
        
#‘定义图片下载函数’
def down_load(src,x,name):
            try:
                
                print('正在下载%s第%d 张'%(name,x))
                urllib.request.urlretrieve(src,'%s%d.jpg'%(name,x))
                x+=1
            except:
                print('Fail to download the %s%d.jpg'%(name,x))
            return x

        
            
                   
                        
if  __name__ == '__main__':
#‘准备保存图片的文件夹'
    location=input('where to store:')#'获得目录名'
    name=input('img name:')
    
    location='e:\\lyx\\python download\\'+location#'自己的下载目录，可以根据需要修改'
    if not os.path.exists(location):#'如果不存在，则创建并切换到这个目录'
        os.makedirs(location) 
        os.chdir(location)
    else:  #'如果存在文件目录，覆盖输入1，放弃并结束程序输入0'
        print('the file is already existed')
        value=int(input('print "1" to go on,or "0"to exit '))
        if value:
            os.chdir(location)
            print("OK")
        elif not value:
            print('Bye-ye')
            os._exit(0)

    #'urls--所有待爬的地址'
    root_url = input('your url:')
    urls = get_url(root_url)
    if urls==None:
        print('on other urls')
    urls.insert(0,root_url)
    print('we have got these urls:')
    for each in urls:
        print(each)

    #'开始从这些相关urls里爬取img地址并下载'
    x=0
    for each in urls:
        x=get_img(each,x,name)
    print('All done') 
    print('the numbers of pictures downloaded is %d:'%x)

        
        

 


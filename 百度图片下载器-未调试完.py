import requests
from bs4 import BeautifulSoup
import re
import os
import time


#'定义寻找页面里所有待爬取img地址并下载，防错机制'
def get_imgurl(url):
    time.sleep(5)
    global x
    global name
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
        r=requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
        links =soup.find('ul',class_='imglist').find_all('a',class_='imglink')
        
        for link in links:
            href=link['href']
            print(href)
            down_load(href)
           
        
        
    except:
        print('fail to deal with the url %s'%url)
    
    
    

#'定义寻找所有待爬取url函数，防错机制'
def get_url(url):
    global count                   
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    r=requests.get(url, headers=headers)
    #'解析获得除主url外其它页面url'
    soup = BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
    links= soup.find_all('a',href=re.compile(r"\/search\/flip\?tn=baiduimage"))#'这步筛选没有直接取得剩余url'
    #'补全url'
        
    while len(undo)<15:

        for link in links:
            url_find='http://image.baidu.com'+link['href']
            strinfo = re.compile(r"\&gsm=.*")
            url_find =strinfo.sub('',url_find)
            
            if url_find not in undo:
               
                undo.add(url_find)
               
                get_url(url_find)
       
        
            
                   
    
              
    
            
        
#‘定义图片下载函数’
def down_load(src):
    time.sleep(5)
    global x
    global name
    print('正在下载%s第%d 张'%(name,x))
    
    try:
        pic= requests.get(src, stream=True)
        
    except requests.exceptions.ConnectionError:
        print( '【错误】当前图片无法下载')
        
    string = name+'%d'%x+'.jpg'
    try:
        with open(string,'wb') as fp:
            fp.write(pic.content)
            x+=1
    except:
        print('%s第%d张图片保存失败'%(name,x))
        
        
      
    

##def where_store():
##    #‘准备保存图片的文件夹'
##    location=input('where to store:')#'获得目录名'
##    
##    
##    location='e:\\lyx\\python download\\picture'+location#'自己的下载目录，可以根据需要修改'
##    if not os.path.exists(location):#'如果不存在，则创建并切换到这个目录'
##        os.makedirs(location) 
##        os.chdir(location)
##    else:  #'如果存在文件目录，覆盖输入1，放弃并结束程序输入0'
##        print('the file is already existed')
##        value=int(input('print "1" to go on,or "0"to exit '))
##        if value:
##            os.chdir(location)
##            print("OK")
##        elif not value:
##            print('Bye-ye')
##            os._exit(0)
            
def main():
    
##    where_store()
    
    
    root_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+name+'&ct=201326592&v=flip'
    get_url(root_url)
    
    
    for each in undo:
        get_imgurl(each)
        
        
    print('All done') 
    print('the numbers of pictures downloaded is %d:'%x) 
        
    
                   
                        
if  __name__ == '__main__':
    global undo
    global name
    global x
    undo=set()
    name=input('img name：')
    x=0
    main()






        
        

 


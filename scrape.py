import requests
from lxml import etree
import re
import os
import time


#'定义寻找页面里所有待爬取img地址并下载，防错机制'
def get_imgurl(url):
    try:
        headers = {'Content-Type': 'application/json; charset=UTF-8',# 因为是ajax请求，格式为json，这个必须指定
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
        r=requests.get(url, headers=headers,timeout=10)
        links=re.findall(r'"objURL":"(.*?)"',r.text)
        for link in links:
            get_img(link)      
    except:
        print('fail to deal with the url %s'%url)
    
    
    

#'定义寻找所有待爬取url函数，防错机制'
def get_url(url):
    global undo                   
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    r=requests.get(url, headers=headers,timeout=2)
    #'解析获得除主url外其它页面url'
    tree = etree.HTML(r.text)
    links = tree.xpath('//*[@id="page"]/a')
    #'这步筛选没有直接取得剩余url'
    #'补全url' 
    while len(undo)<15:
        for link in links:
            url_find='http://image.baidu.com'+link.attrib['href']
            strinfo = re.compile(r"\&gsm=.*")
            real_url =strinfo.sub('',url_find)   
            if real_url not in undo:
                undo.add(real_url)
                try:
                    get_url(real_url)
                except:
                    continue
   
        
          
#‘定义图片下载函数’
def get_img(src):
    time.sleep(1)
    global x
    global name
    print('正在下载%s第%d 张'%(name,x))
    
    try:
        pic= requests.get(src, stream=True,timeout=2)
        
    except requests.exceptions.ConnectionError:
        print( '【错误】当前图片无法下载')
        
    string = name+'%d'%x+'.jpg'
    try:
        with open(string,'wb') as fp:
            fp.write(pic.content)
            x+=1
    except:
        print('%s第%d张图片保存失败'%(name,x))
        
        
      
    

def where_store():
    #‘准备保存图片的文件夹'
    location=input('where to store:')#'获得目录名'
    location='e:\\lyx\\python download\\picture'+location#'自己的下载目录，可以根据需要修改'
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
##            
def main():
    global undo
    where_store()
    root_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+name+'&ct=201326592&v=flip'
    print('working,print Ctrl+c to stop if you like')
    get_url(root_url)
    for each in undo:
        get_imgurl(each)    
    print('All done') 
    print('the numbers of pictures downloaded is %d:'%x) 
        
    
                   
                        
if  __name__ == '__main__':
##    global undo
##    global name
##    global x
    undo=set()
    name=input('img name：')
    x=0
    main()






        
        

 


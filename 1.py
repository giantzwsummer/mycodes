import requests
from lxml import etree
import re
import os
import time


#'定义寻找页面里所有待爬取img地址并下载，防错机制'
def get_imgurl(url):
##    global x
##    global name
   
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
               ,'X-Requested-With':'XMLHttpRequest'}
    data={'src':'pc','page':'searchresult'}
    
    r=requests.post(url,data=data, headers=headers)
    urls=re.findall(r'"objURL":"(.*?)"',r.text)
    
    for url in urls:
        
        print(url)
##   
##    tree = etree.HTML(r.text)
##    
##    links = tree.xpath('//*[@id="imgid"]/ul/li[1]')
    
##url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&sf=1&fmq=1447473655189_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%95%BF%E8%80%85%E8%9B%A4'
    
    
    
    
   
    
  

   

##    for link in links:
##        src=link['href']
##        print(src)
####    except:
####        print('fail to down')
    
url=r'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%A3%81%E7%BA%B8&ct=201326592&v=flip'
get_imgurl(url)
##&gsm=20000003c

import urllib.request
from bs4 import BeautifulSoup
import re
import os
#‘准备保存图片的文件夹'
os.mkdir('pictures')
os.chdir(os.path.join(os.getcwd(), 'pictures'))
#'准备一个空列表，加入开始url'
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
        return(response)
response=get_url(url)
if response==None:
        print('error shuntdown')


soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
urllinks= soup.find_all('a',href=re.compile(r'/p/\d+.pn='))


for link in urllinks:
   
    linkurl='http://tieba.baidu.com'+link['href']
    url_all.append(linkurl)
print('the urls you wanted are blew:')
urls=sorted(set(url_all))
print(urls)
   
y=0
for a_url in urls:
        

        response_= get_url(a_url)
       
        soup = BeautifulSoup(response_,'html.parser',from_encoding='utf-8')
        links =soup.find_all('img',class_='BDE_Image',src=re.compile(r"\.jpg"))
        
        x=0
        for link in links:
            src=link['src']
##            print(src)


            try:
                
                print('正在下载'+a_url+'第 %s张'%x)
                urllib.request.urlretrieve(src,'%s%s.jpg'%(y,x))
            except:
                print('Fail to download'+ '%s.jpg'%x)
            x+=1
        y+=1


 


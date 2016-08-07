import requests
import urllib.request
urllinks=list()
url='http://tieba.baidu.com/photo/g/bw/picture/list?kw=%E9%A9%B4%E5%8F%8B&alt=jview&rn=200&tid=3549202764&pn=1&ps=1&pe=40&info=1&_=1469771702213'

r = requests.get(url)
print(r.status_code)
data = r.json()
for pic_list in data['data']['pic_list']:
    urllink=pic_list['purl']
    urllinks.append(urllink)
print('the src wanted are blew: ')
x=0
for urllink in urllinks:
    print(urllink)
    try:
        print('正在下载第%d张'%x)
        urllib.request.urlretrieve(urllink,'%d.jpg'%x)
        x+=1
    except:
        print('%d.jpg'%x+'failed')
    
print('total number is %d'%x)

            
                                   
    

    
    


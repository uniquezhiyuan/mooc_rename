from bs4 import BeautifulSoup
import re
import os

soup=BeautifulSoup(open('c:/data/html/mooc.html',encoding='utf8'))
video_tag=soup.find_all('li',class_='list-group-item videoBtn shdVideo')
video_url=[url.a.attrs['href'] for url in video_tag]
video_name=[url.a.string for url in video_tag]
'''传方法
def has_href_but_no_rel(tag):
    return tag.has_attr('href') and not tag.has_attr('rel')

soup.find_all(has_href_but_no_rel)
'''
doc_tag=soup.find_all(href=re.compile('pdf'))
doc_url=[url.attrs['href'] for url in doc_tag]
doc_name=[url.string for url in doc_tag]

old_name=[href.split('/')[-1] for href in video_url]
new_name=video_name

for file in os.listdir('c:/迅雷下载/mooc'):
    for name in old_name:
        if file==name:
            try:
                os.rename('c:/迅雷下载/mooc/'+file,'c:/迅雷下载/mooc/'+new_name[old_name.index(name)]+'.flv')
            except:
                os.rename('c:/迅雷下载/mooc/'+file,'c:/迅雷下载/mooc/'+new_name[old_name.index(name)]+'_'+'.flv')

file=open('c:/data/order.txt','w') #text file catageory
for i in new_name:
    file.write(i)
    file.write('\n')

file.close()

'''
old_name=['0.txt','1.txt','2.txt','3.txt']
new_name=['A.txt','B.txt','C.txt','D.txt']
os.rename('c:/迅雷下载/test/d.txt','c:/迅雷下载/test/ch.txt')
'''


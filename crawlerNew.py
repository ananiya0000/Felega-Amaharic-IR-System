# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:36:58 2022

@author: anani
"""

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    i=1
    page=1
    while page <=max_pages:
        url='https://amharic.voanews.com/z/3661?p='+str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,features='lxml')
        for link in soup.findAll('a',{'class':'img-wrap'}):
            content=""
            href=link.get('href')
            hrefmain="https://amharic.voanews.com"+str(href)
            title=link.get('title')
            if(str(title)=="None"):
                for innerlink in link.findAll('h4'):
                    title=innerlink.get('title')
            urlInner=str(hrefmain)
            source_code_inner=requests.get(urlInner)
            plain_text_inner=source_code_inner.text
            soup_inner=BeautifulSoup(plain_text_inner,features='lxml')
            for link_inner in soup_inner.findAll('p'):
                if(str(link_inner.string)!='None'):
                    content=content+str(link_inner.string)+"\n"
            
            doc=open("./pages/Document"+str(i)+".txt","w",encoding="utf-8")  
            doc.write(str(title)+"\n\n\n"+str(content))
            doc.close()
            i+=1    
        page+=1

trade_spider(2)
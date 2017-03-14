# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:        
        r=requests.get(url)
        r.raise_for_status()
        return r.content
    except:
        return ""

        
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').find_all('tr'):
        data=tr('td')
        ulist.append([data[1].string,data[2].string])
        

def printUnivList(uList,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print (tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=uList[i]
        print (tplt.format(i,u[0],u[1],chr(12288)))
    print ("Suc "+str(num))

    

uinfo = []
url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
html=getHTMLText(url)
fillUnivList(uinfo,html)
printUnivList(uinfo,20)


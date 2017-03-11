# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.baidu.com")
soup=BeautifulSoup(r.content,"html.parser")
print (soup.title)
print (soup.a.name)
print (soup.a.parent.name)

tag=soup.a
print (tag)
print (tag.attrs)
print (tag.attrs['class'])
print (tag.attrs['href'])
print (tag.string)

newsoup=BeautifulSoup("<b><!--this is a comment--></b><p>this is not a comment</p>"
                      ,"html.parser")
print (newsoup.b.string)
print (type(newsoup.b.string))
print (newsoup.p.string)
print (type(newsoup.p.string))

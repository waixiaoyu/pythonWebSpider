import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.baidu.com")
soup=BeautifulSoup(r.content,"html.parser")

#for link in soup.find_all('a'):
#    print (link.get('href'))
    
    

for link in soup.find_all(True):
    print (link.name)
    
    
import re
for tag in soup.find_all(re.compile('b')):
    print (tag.name)
    
print (soup.find_all('a','mnav'))
print (soup.find_all(id='cp'))
print (soup.find_all(id=re.compile('cp')))

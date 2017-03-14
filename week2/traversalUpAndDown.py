import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.baidu.com")
soup=BeautifulSoup(r.content,"html.parser")
#==============================================================================
# down
#==============================================================================

#print (soup.head)
#print (soup.head.contents)
#print (len(soup.body.contents))
#
#for child in soup.body.contents:
#    print (child)


#==============================================================================
# up
#==============================================================================

#print ('\n')    
#print ('\n')    
#print ('\n')
#print (soup.title.parent)
#
#for parent in soup.a.parents:
#    if parent is None:
#        print (parent)
#    else :
#        print (parent.name)
#        
        
#==============================================================================
# sibling
#==============================================================================
print (soup.a.next_sibling.next_sibling)
print (soup.a.previous_sibling)

for sibling in soup.a.next_siblings:
    print (sibling)
    
#==============================================================================
# pretiffy     
#==============================================================================
demo=r.text
print (demo)
print (soup.prettify())
print (soup.a.prettify())

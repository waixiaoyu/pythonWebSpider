# -*- coding: utf-8 -*-

import re
match=re.search(r'[1-9]\d{1,5}','AAA 100061 BIT')
#if match:
#    print (match.group(0))
    

ls=re.findall(r'[1-9]\d{1,5}','100061 BIT 123456')
#print (ls)

#ls=re.split(r'[1-9]\d{1,5}','ASD100061BIT123456TSU')
#print (ls)
#ls=re.split(r'[1-9]\d{1,5}','ASD100061BIT123456TSU',1)
#print (ls)
#for m in re.finditer(r'[1-9]\d{1,5}','ASD100061BIT123456TSU'):
#    if m:
#        print (m.group(0))
        
        
#print (re.sub(r'[1-9]\d{1,5}','XXXXXX','ASD100061BIT123456TSU'))


print (match.string)
print (match.re)
print (match.pos)
print (match.endpos)
print (match.group(0))
print (match.start())
print (match.end())
print (match.span())
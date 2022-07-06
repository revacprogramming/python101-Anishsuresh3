# Using Web Services
# https://www.py4e.com/lessons/servces
import urllib.request
import xml.etree.ElementTree as et
fh=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1550210.xml')
data=fh.read()
tree=et.fromstring(data)
lst=tree.findall('comments/comment') 
sum=0
for items in lst:
    num=int(items.find('.//count').text)
    sum+=num

print(sum)
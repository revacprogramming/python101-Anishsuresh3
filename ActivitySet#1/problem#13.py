# Network Programming
# https://www.py4e.com/lessons/network

import socket
from bs4 import BeautifulSoup
from urllib.request import urlopen
url=input('enter the url- ')
counts=int(input('enter count: '))
position=int(input('enter position: '))
for i in range(counts):
    count=0
    html=urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    # print(count)
    tags = soup('a')
    for tag in tags:
        if count<position:
            # print(tag.get('href'))
            count+=1
            url=tag.get('href')
    print('Retrieving:',url)
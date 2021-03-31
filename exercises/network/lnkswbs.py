# lnkswbs.py
# Autograder: Following Links with BeautifulSoup on https://www.py4e.com/lessons/network

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import time

url = input('Enter URL: ')
# if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/known_by_Johndean.html'
count = int(input('Enter count: ')) + 1 # total is one bigger than count
pos = int(input('Enter position: ')) - 1 # third from index 1 being first

start = time.time()
for i in range(count):
    print('Retrieving', url)
    html = urlopen(url).read() # bytes
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # if i == count - 1: break    
    url = [ tag.get('href') for tag in tags ][pos]  

# name = re.findall('known_by_(\w+)',url)[0]
# print(dir(name))
# print(name)
# print(url)

end = time.time()
print(end - start)
# xml.py
# https://www.py4e.com/lessons/servces

import urllib.request
import xml.etree.ElementTree as ET
import time

url = input('Enter location: ')
# if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1172172.xml'

start = time.time()
data = urllib.request.urlopen(url).read() # bytes
print('Retrieving', url)
print('Retrieved', len(data))
tree = ET.fromstring(data) # bytes are accepted too?
# XPath support
# https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath 
lst = [ int(el.text) for el in tree.findall('.//count') ]
count = len(lst)
result = sum(lst)
print('Count:', count)
print('Sum:', result)

end = time.time()
print(end-start)

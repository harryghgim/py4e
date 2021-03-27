# datafromjson.py
# Autograder: Extract Data from JSON on https://www.py4e.com/lessons/servces

from urllib.request import urlopen
import time
import json

url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1172173.json'
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print('Retrieving', url)
dt = urlopen(url).read() # bytes
print('Retrieved', len(dt))
jsdt = json.loads(dt) # dict
lst = [ int(dt['count']) for dt in jsdt['comments'] ]
count = len(lst)
sm = sum(lst)

print('Count:', count)
print('Sum:', sm)


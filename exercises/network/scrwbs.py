# scrwbs.py
# Autograder: Scraping HTML Data with BeautifulSoup on https://www.py4e.com/lessons/network

import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')

start = time.time()
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1172170.html'
# html = urlopen('http://py4e-data.dr-chuck.net/comments_42.html').read() # bytes
html = urlopen(url).read() # bytes
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
nums = [ int(span.string) for span in soup('span') ]
print( 'Count', len(tags) )
print( 'Sum', sum(nums) )
    
end = time.time()

print(end-start)
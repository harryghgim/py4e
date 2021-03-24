# regeximp.py
# more efficient and elegant than regex.py
# Autograder: Regular Expressions on https://www.py4e.com/lessons/regex

import re
import time

start = time.time()
# fhand = open('regex_sum_42.txt') # 445833
fhand = open('regex_sum_1172168.txt')

print( sum( [ int(sn) for sn in re.findall( '\d+', fhand.read() ) ] ) )
# print( sum( map( int, re.findall( '\d+', fhand.read() )) ) )

end = time.time()
print(end - start)
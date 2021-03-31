# regex.py
# Autograder: Regular Expressions on https://www.py4e.com/lessons/regex

import re
import time

start = time.time()

lst = list()
# fhand = open('regex_sum_42.txt') # 445833
fhand = open('regex_sum_1172168.txt')
for line in fhand:
    line = line.rstrip()
    slst = re.findall('\d+', line)
    lst.extend(slst)

print(sum(map(int, lst)))

end = time.time()
# print(end - start)
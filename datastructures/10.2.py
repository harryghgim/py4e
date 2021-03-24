# 10.2.py
# Click Autograder: Exercise 10.2 on https://www.py4e.com/lessons/tuples

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    khr = line.split()[5].split(':')[0]
    counts[khr] = counts.get(khr, 0) + 1

kvlst = sorted(counts.items())
for k,v in kvlst:
    print(k,v)

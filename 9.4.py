# 9.4.py
# Autograder: Exercise 9.4 on https://www.py4e.com/lessons/dictionary

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict() 

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    # print(line) # line starts with 'From '
    sender = line.split()[1]
    # print(sender)
    counts[sender] = counts.get(sender, 0) + 1

msender = None
mcount = None
for sender, count in counts.items():
    if msender is None or count > mcount: # statement before 'or' runs only once
        msender = sender
        mcount = count

print(msender, mcount)
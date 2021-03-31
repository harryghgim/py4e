# 8.4.py
# https://www.py4e.com/lessons/lists

fname = input("Enter file name: ") # romeo.txt
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip() # remove '\n' at the EOL
    llst = line.split() # make a list out of words in line
    for word in llst:
        if word in lst: continue
        # print(word)
        lst.append(word)        

lst.sort()
print(lst)
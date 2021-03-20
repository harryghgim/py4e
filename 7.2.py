# 7.2.py
# https://www.py4e.com/lessons/files

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ") # mbox-short.txt
fh = open(fname) # file handler object
sm = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # line = line.rstrip()
    # print(line) # line that startswith "X-DSPAM-Confidence:"    
    idx = line.rfind(' ')
    fn = float(line[idx+1:]) # 0.8475
    # print(fn)
    sm += fn
    count += 1

avg = sm / count

print("Average spam confidence:", avg)
# print("Done")

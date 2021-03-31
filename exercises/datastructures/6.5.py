text = "X-DSPAM-Confidence:    0.8475"
stt = text.find(' ')
num = float(text[stt:].lstrip())
print(num)
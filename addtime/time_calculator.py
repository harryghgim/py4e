# project 2: Time Calculator
# question: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
# answer: https://replit.com/@harryghgim/boilerplate-time-calculator#time_calculator.py

def add_time(start, duration, startday=None):
    tm, per = start.split()

    ho, mo = list( map( int, tm.split(':') ) )
    if per == 'PM': ho = ho + 12
    ht, mt = list( map( int, duration.split(':') ) )

    hh = ho + ht
    mm = mo + mt
    if mm > 60:
        mm = mm - 60
        hh += 1

    bday = 0
    bmsg = None
    print("line 65:", hh)

    quot, rem = hh // 24, hh % 24
    if rem == 0: rem = 12
    print("line 68:", quot, rem)

    if quot > 0:
        bday += quot
        hh = rem

    if bday > 1:
        bmsg = f" ({bday} days later)"
    elif bday == 1:
        bmsg = f" (next day)"

    if hh > 12: 
        per = 'PM'
        hh = hh - 12
    else: 
        per = 'AM'

    ntime = f"{hh}:{mm:02d} {per}"

    if bmsg is not None: ntime += bmsg
    
    return ntime

# test 1, test 2, test 3, test 4, test 5, test 6
# start, duration = "3:30 PM", "2:12" 
# start, duration = "11:55 AM", "3:12" 
# start, duration = "9:15 PM", "5:30"
# start, duration = "11:40 AM", "0:25"
# start, duration = "2:59 AM", "24:00"
# start, duration = "11:59 PM", "24:05"
# start, duration = "8:16 PM", "466:02"
start, duration = "5:01 AM", "0:00"

tm, per = start.split()

ho, mo = list( map( int, tm.split(':') ) )
if per == 'PM': ho = ho + 12
ht, mt = list( map( int, duration.split(':') ) )

hh = ho + ht
mm = mo + mt
if mm > 60:
    mm = mm - 60
    hh += 1

bday = 0
bmsg = None
print("line 65:", hh)

quot, rem = hh // 24, hh % 24
if rem == 0: rem = 12
print("line 68:", quot, rem)

if quot > 0:
    bday += quot
    hh = rem

if bday > 1:
    bmsg = f" ({bday} days later)"
elif bday == 1:
    bmsg = f" (next day)"

if hh > 12: 
    per = 'PM'
    hh = hh - 12
else: 
    per = 'AM'

ntime = f"{hh}:{mm:02d} {per}"

if bmsg is not None: ntime += bmsg

print(ntime)

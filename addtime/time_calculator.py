# project 2: Time Calculator
# question: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
# answer: https://replit.com/@harryghgim/boilerplate-time-calculator#time_calculator.py

def add_time(start, duration, startday=None):
    tm, per = start.split()

    ho, mo = list( map( int, tm.split(':') ) )
    ht, mt = list( map( int, duration.split(':') ) )

    hh = ho + ht
    mm = mo + mt
    bday = 0
    bmsg = None
    if mm > 60:
        mm = mm - 60
        hh += 1

    if hh > 24 and per == 'PM':
        hh = hh - 24
        per = 'AM'
        bday = bday + 2

    if hh > 12 and per == 'AM':
        per = 'PM'
        hh = hh - 12

    if hh > 12 and per == 'PM':
        per = 'AM'
        hh = hh - 12
        bday = bday + 1

    ntime = f"{hh}:{mm:02d} {per}"

    if bday > 1: bmsg = f" ({bday} days later)"
    elif bday == 1: bmsg = ' (next day)'

    if bmsg is not None: ntime += bmsg
    
    return ntime

# test 1, test 2, test 3, test 4, test 5, test 6
# start, duration = "3:30 PM", "2:12" 
# start, duration = "11:55 AM", "3:12" 
# start, duration = "9:15 PM", "5:30"
# start, duration = "11:40 AM", "0:25"
# start, duration = "2:59 AM", "24:00"
# start, duration = "11:59 PM", "24:05"
start, duration = "8:16 PM", "466:02"

tm, per = start.split()

ho, mo = list( map( int, tm.split(':') ) )
ht, mt = list( map( int, duration.split(':') ) )

hh = ho + ht
mm = mo + mt
bday = 0
bmsg = None
if mm > 60:
    mm = mm - 60
    hh += 1

quot, rem = hh // 24, hh % 24
perquot = hh // 12
print(quot, rem)
print(perquot)
if quot > 0: 
    bday += quot
    if rem > 12:
        per = 'PM'
        hh = rem - 12
    
# if hh > 24 and per == 'PM':
#     hh = hh - 24
#     per = 'AM'
#     # bday = bday + 2

# if hh > 12 and per == 'AM':
#     per = 'PM'
#     hh = hh - 12

# if hh > 12 and per == 'PM':
#     per = 'AM'
#     hh = hh - 12
    # bday = bday + 1

ntime = f"{hh}:{mm:02d} {per}"

if bday > 1: bmsg = f" ({bday} days later)"
elif bday == 1: bmsg = ' (next day)'

if bmsg is not None: ntime += bmsg

print(ntime)

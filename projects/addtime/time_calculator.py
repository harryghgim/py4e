# Time Calculator
# question: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
# answer: https://replit.com/@harryghgim/boilerplate-time-calculator#time_calculator.py
# run "python3 main.py" to check if the function below passess all the tests 
# defined in test_module.UnitTests

def add_time(start, duration, startday=None):
    DAYS = ['Sunday', 'Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",]

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

    quot, rem = hh // 24, hh % 24

    if quot > 0:
        bday = quot

    hh = rem

    if hh > 12: 
        per = 'PM'
        hh = hh - 12
    elif hh == 12:
        per = 'PM'
    else: # hh < 12
        per = 'AM'
        if hh == 0:
            hh = 12

    if bday > 1:
        bmsg = f"({bday} days later)"
    elif bday == 1:
        bmsg = f"(next day)"

    ntime = f"{hh}:{mm:02d} {per}"

    if startday is not None:
        startday = startday.capitalize()
        dayidx = DAYS.index(startday) # 1
        dayidx = (dayidx + bday) % 7
        tday = DAYS[dayidx]
        ntime += ', ' + tday

    if bmsg is not None: 
        ntime += ' ' + bmsg
        
    return ntime
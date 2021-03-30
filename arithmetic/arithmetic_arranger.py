# Arithmetic FormatterPassed
# question: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
# answer: https://replit.com/@harryghgim/boilerplate-arithmetic-formatter#arithmetic_arranger.py

def arithmetic_arranger(problems, answer=False):

    first = ''
    second = ''
    third = ''
    fourth = ''
    gap = ' ' * 4

    if len(problems) > 5: # test 2
        return "Error: Too many problems."

    for astr in problems:

        asdg, oper, bsdg = astr.split()

        if oper not in ['+', '-']: # test 3
            return "Error: Operator must be '+' or '-'." 

        try: result = str(eval(astr)) # test 5
        except: return "Error: Numbers must only contain digits."
                    
        alen, blen = len(asdg), len(bsdg)

        if alen > 4 or blen > 4: # test 4
            return "Error: Numbers cannot be more than four digits."

        nus = max(alen, blen) + 2 # number of underscore

        first += asdg.rjust(nus) + gap
        if alen < blen: 
            second += oper + ' ' + bsdg + gap
        else:
            second += oper + ' ' + bsdg.rjust(alen) + gap
        third += nus * '-' + gap
        fourth += result.rjust(nus) + gap

    lst = list( map( str.rstrip, [first, second, third, fourth] ) )
    
    if answer: # test 6
        return '\n'.join(lst)
    return '\n'.join(lst[:3])
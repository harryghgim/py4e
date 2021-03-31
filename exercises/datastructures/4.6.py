def computepay(h,r):
    pay = 0
    if h <= 40:
        pay = h * r
    else: # h > 40
        reg = r * 40 
        over = r * 1.5 * (h - 40)
        pay = reg + over
    return pay

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
p = computepay(hrs,rate)
print("Pay",p)
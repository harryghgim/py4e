hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))
if h > 40:
    pay = 40 * rate + (h - 40) * rate * 1.5
print(pay)

# improved
# hrs = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))
# if hrs > 40:
#     print("overtime")    
#     reg = hrs * rate
#     otp = (hrs - 40.0) * (rate * 0.5)
#     pay = reg + otp
# else:
#     print("regular")
#     pay = hrs * rate
# print(pay)
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        num = int(num) # check if num is integer
    except Exception as e:
        print("Invalid input")
        continue # if not go back to first loop

    if largest is None or num > largest: 
        largest = num

    if smallest is None or num < smallest: 
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
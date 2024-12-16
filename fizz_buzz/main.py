# for loop to print 1-100
for num in range(1, 101):
    # Multiples of 3 and 5
    if num % 15 == 0:
        print("FizzBuzz", end=",")
    # Multiples of 3
    elif num % 3 == 0:
        print("Fizz", end=",")
        # Multiples of 5
    elif num % 5 == 0:
        print("Buzz", end=",")
    else:
        print (num, end=",")
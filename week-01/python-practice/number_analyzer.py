user_number = int(input("Enter number: "))

if user_number < 0:
    if user_number % 2 == 0:
        print("The number is negative even")
    else:
        print("The number is negative odd")
elif user_number > 0:
    if user_number % 2 == 0:
        print("The number is positive even")
    else:
        print("The number is positive odd")
else:
    print("The number is zero")
user_year = int(input("Please, enter the year: "))

if user_year % 4 != 0:
    print("This is not a leap year")
elif user_year % 100 == 0 and user_year % 400 != 0:
    print("This is not a leap year")
else:
    print("This is a leap year")
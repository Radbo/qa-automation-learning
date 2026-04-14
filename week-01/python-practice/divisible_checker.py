user_number = int(input("Enter number: "))
    
if user_number % 3 == 0 and user_number % 5 == 0:
    print("divisible by both")
elif user_number % 3 == 0:
    print("divisible by 3")
elif user_number % 5 == 0:
    print("divisible by 5")
else:
    print("divisible by none")
# Task: Reverse a number
# The user enters a positive number.
# Print its digits in reverse order as a string.

# Solution 1
# user_number = input("Enter a positive number: ")
# user_number_reversed = user_number[::-1]
# print(user_number_reversed)

# Solution 2 with while loop
user_number = int(input("Enter a positive number: "))
reversed_number = ""
digit = 0

while user_number > 0:
    digit = user_number % 10
    reversed_number += str(digit)
    user_number = user_number // 10
    
print(reversed_number)
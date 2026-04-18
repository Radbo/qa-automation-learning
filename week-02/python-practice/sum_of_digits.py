# Task: Sum of the digits of a number
# input: The user enters a positive number.
# output: Find the sum of its digits using a while loop.

user_number = int(input("Enter positive number: "))
digit = 0
sum_of_digits = 0

while user_number > 0:
    digit = user_number % 10
    sum_of_digits += digit
    user_number = user_number // 10

print(sum_of_digits)
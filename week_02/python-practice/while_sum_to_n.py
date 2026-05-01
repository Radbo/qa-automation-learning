user_number = int(input("Please, enter a number: "))
user_number_for_sum = user_number
sum_of_numbers = 0

while user_number_for_sum > 0:
    sum_of_numbers += user_number_for_sum
    user_number_for_sum -= 1

print(sum_of_numbers)
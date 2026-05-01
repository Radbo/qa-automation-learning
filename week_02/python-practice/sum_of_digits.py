def sum_of_digits(*, number: int) -> int:
    total = 0
    number = abs(number)
    while number > 0:
        total += number % 10
        number //=  10 
    return total

user_number = int(input("Enter a number: "))
result = sum_of_digits(number = user_number)
print(result)
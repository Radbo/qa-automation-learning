def count_digits(*, number: int) -> int:
    counter = 1
    number = abs(number)

    while number >= 10:
        number //= 10
        counter += 1
    
    return counter


user_number = int(input("Enter a number: "))
result = count_digits(number = user_number)
print(result)
def reverse_number(*, number: int) -> str:
    if number < 0:
        return "-" + str(abs(number))[::-1]
    return str(number)[::-1]

user_number = int(input("Enter a number: "))
result = reverse_number(number = user_number)
print(result)
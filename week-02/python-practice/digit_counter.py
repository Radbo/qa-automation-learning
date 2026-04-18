# user_number = str(input("Enter a positive integer: "))
# counter = 0

# for letter in user_number:
#     counter += 1

# print(counter)

user_number = int(input("Enter a positive integer: "))
counter = 1

while user_number >= 10:
    user_number = user_number // 10
    counter += 1

print(counter)

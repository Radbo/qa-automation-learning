user_roles = ("admin", "editor", "viewer")

role_1, role_2, _ = user_roles

user = ("Tony", 25, "driver")
name, _, job, = user
print(f"My name is {name}, and I'm a {job}.")

some_numbers = (1, 2, 3, 4, 5)

print(f"First number in tuple is {some_numbers[0]}")
print(f"last number is {some_numbers[-1]}")
print(f"length is {len(some_numbers)}")

if 10 in some_numbers:
    print("This tuple contains 10")
else:
    print("This tuple does not contain 10")
user_age = int(input("Enter age: "))

if user_age < 0:
    print("Age can't be negative")
elif user_age < 13:
    print("You are a child")
elif user_age < 18:
    print("You are a teenager")
elif user_age < 65:
    print("You are an adult")
else:
    print("You are a senior")
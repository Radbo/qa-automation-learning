correct_password = "python123" 
attempt_counter = 3 
approved = False

while attempt_counter > 0:
    user_password_input = input("Enter password: ")
    attempt_counter -= 1
    if user_password_input == correct_password:
        approved = True
        print("Access granted")
        break
    else:
        if attempt_counter > 0: 
            print(f"The password is incorrect. Try again. Remaining attempts: {attempt_counter}")

if not approved:
    print("The password is incorrect. You have no more attempts left. Access denied.")
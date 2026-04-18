counter_user_input = 0

while True:
    user_number = (input("Enter a number or 'stop': "))
    if user_number == "stop":
        break
    user_number = int(user_number)
    counter_user_input += 1
    if counter_user_input == 1:
        max_number = user_number
    if user_number > max_number:
        max_number = user_number
     
if counter_user_input == 0:
    print("You have not entered any numbers")
else:   
    print(f"The user entered numbers: {counter_user_input}. The largest number entered by the user {max_number} ")
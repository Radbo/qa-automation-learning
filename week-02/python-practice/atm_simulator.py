balance = 0


def menu_number_navigation(*, current_choice: int, first_number_item: int, last_item_number: int):
    number_of_menu_item = range(first_number_item, last_item_number + 1)
    if current_choice not in list number_of_menu_item:
        return print("Please enter a valid number")
    else:
        return current_choice


# def amount_verification(*, number: str) -> str, bool, int:
#     if number.isdigit():
#         number = int(number)
#         if number < 0:
#             return print("Please enter a positive number")
#         else:
#             return number
#     else:
#         return print("Please enter a number")


# def making_a_deposit(*, amount: int) -> int:
#     return balance += amount

# def making_a_withdraw(*, amount: int) -> int:
#     return balance -= amount

# def checking_balance(*, coomand: bool) -> int:
#     return print(balance)


while True:
    print("================")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("================")
    user_choice = (input("Select a menu item by entering its number: "))
    print(menu_number_navigation(current_choice=user_choice, first_number_item: 1, last_item_number: 4))


    
    # if user_choice == 2:
    #     user_amount = (input("Enter the amount: "))
    #     if not amount_verification(user_amount):
    #         print("You entered an incorrect value")
    #         print("================")
    #     user_amount = int(user_amount)
    #     balance += user_amount

    # if user_choice == 3:
    #     user_withdraw = (input("Enter the amount: "))
    #     if not amount_verification(user_withdraw):
    #         print("You entered an incorrect value")
    #         print("================")
    #     user_withdraw = int(user_withdraw)
    #     if user_withdraw > balance:
    #         print("There are not enough funds in your account.")
    #         print("================")
    #     else:
    #         balance -= user_withdraw
    
    # if user_choice == 4:
    #     break
balance = 0

def integer_input_check(*, user_input: str):
    if user_input.isdigit() and int(user_input) > 0:
        return True, int(user_input)
    return False, user_input


def menu_navigation(*, user_choice: str, first_menu_item_number: int, last_menu_item_number: int):
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if first_menu_item_number <= user_choice <= last_menu_item_number:
            return True, user_choice
        else:
            return False, user_choice
    else:
        return False, user_choice


def balance_checker():
    return balance


def deposit_maker(*, amount: str):
    integer_input_check_success, user_amount = integer_input_check(user_input = amount)
    if integer_input_check_success:
        global balance 
        balance += user_amount
        return True, balance
    else:
        return False, balance

def withdraw_maker(*, amount: str):
    integer_input_check_success, user_withdraw = integer_input_check(user_input = amount)
    if integer_input_check_success:
        global balance 
        if user_withdraw > balance:
            return False, balance
        else:
            balance -= user_withdraw
            return True, balance
    else:
        return None, balance

while True:
    print("================")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("================")
    user_choice = (input("Select a menu item by entering its number: "))
    print("================")
    menu_navigation_success, user_choice = menu_navigation(user_choice = user_choice, first_menu_item_number = 1, last_menu_item_number = 4)
    if menu_navigation_success:
        if user_choice == 1:
            print("Balance")
            print(f"Your balance is: {balance_checker()}")
        elif user_choice == 2:
            print("Deposit")
            user_amount = (input("Enter the deposit amount: "))
            deposit_maker_success, user_amount = deposit_maker(amount = user_amount)
            if deposit_maker_success:
                print("The deposit has been accepted.")
            else:
                print("Incorrect entered value!") 
        elif user_choice == 3:
            print("Withdraw")
            user_withdraw_amount = (input("Enter the withdraw amount: "))
            user_withdraw_amount_success, user_withdraw_amount = withdraw_maker(amount = user_withdraw_amount)
            if user_withdraw_amount_success is None:
                print("Incorrect entered value!")
            elif user_withdraw_amount_success:
                print("The withdraw has been accepted.")
            else:
                print("There are insufficient funds in your account")
        elif user_choice == 4: 
            print("Exit")
            break
    else:
        print("Incorrect entered value!") 
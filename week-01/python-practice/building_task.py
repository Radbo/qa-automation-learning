user_flat = (input("Please, enter flat number: ").strip())

if user_flat.isdigit():
    user_flat = int(user_flat)
    if user_flat > 0 and user_flat <= 100:
        user_entrance = (((user_flat - 1) // 20) + 1)
        user_flat_number_in_entrance = (((user_flat - 1) % 20) + 1)
        user_floor = (((user_flat_number_in_entrance - 1) // 4) + 1)
        print("Entrance number", user_entrance)
        print("Floor number", user_floor)
    else:
        print("Please, enter flat number from 1 to 100")
else:
    print("Please, enter flat number")
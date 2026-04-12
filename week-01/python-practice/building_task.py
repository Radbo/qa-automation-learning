user_flat = int(input("Please, enter flat number: "))

if user_flat <= 0 or user_flat > 100:
    print("Please, enter flat number from 1 to 100")
else:
    user_entrance = (((user_flat - 1) // 20) + 1)
    user_flat_number_in_entrance = (((user_flat - 1) % 20) + 1)
    user_floor = (((user_flat_number_in_entrance - 1) // 4) + 1)
    print("Entrance number", user_entrance)
    print("Floor number", user_floor)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "is_active": True},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "is_active": False},
    {"id": 3, "name": "", "email": "invalid-email", "is_active": True},
    {"id": 4, "name": "Diana", "email": "diana@example.com", "is_active": True},
    {"id": 5, "name": "Ethan", "email": "ethan.example.com", "is_active": False},
    {"id": 6, "name": "Fiona", "email": "fiona@example.com", "is_active": "yes"},
    {"id": "7", "name": "George", "email": "george@example.com", "is_active": True},
    {"id": 8, "name": None, "email": "hannah@example.com", "is_active": False},
    {"id": 9, "name": "Ivan", "email": "", "is_active": True},
    {"id": 10, "name": "Julia", "email": "julia@example.com", "is_active": False},
    {"id": 11, "name": "Kevin", "email": "kevin@example", "is_active": True},
    {"id": 12, "name": "Laura", "email": "laura@example.com", "is_active": None},
    {"id": 13, "name": "Mike", "email": "mike@example.com", "is_active": True},
    {"id": 14, "name": "Nina", "email": "nina@example.com", "is_active": False},
    {"id": 15, "name": "Oscar", "email": "@example.com", "is_active": True},
    {"id": 16, "name": "Paula", "email": "paula@", "is_active": False},
    {"id": 17, "name": "Quentin", "email": "quentin@example.com", "is_active": 1},
    {"id": 18, "name": "Rachel", "email": "rachel@example.com"},
    {"name": "Steve", "email": "steve@example.com", "is_active": True},
    {"id": 20, "name": "Tina", "email": "tina@example.com", "is_active": False},
]


def id_valid_checker(user: dict) -> tuple[bool, str]:
    user_id = user.get("id")

    if user_id == None:
        return False, "id is missing"
    elif type(user_id) != int:
        return False, "id is not integer"
    elif user_id <= 0:
        return False, "id must be greater than 0"
    else:
        return True, "user id is valid"


def name_valid_checker(user: dict) -> tuple[bool, str]:
    user_name = user.get("name")

    if user_name == None:
        return False, "user name is missing"
    elif not user_name:
        return False, "user name is empty"
    elif type(user_name) != str:
        return False, "user name is not string"
    else:
        return True, "user name is valid"


def email_valid_checker(user: dict) -> tuple[bool, str]:
    user_email = user.get("email")

    if user_email == None:
        return False, "user email is missing"
    elif type(user_email) != str:
        return False, "user email is not string"
    elif not user_email:
        return False, "user email is empty"
    elif user_email.count("@") != 1:
        return False, "user email must contain exactly one @"
    else:
        email_parts = user_email.split("@")
        email_local_part = email_parts[0]
        email_domain_part = email_parts[1]

        if not email_local_part:
            return False, "user email local part is empty"
        elif not email_domain_part:
            return False, "user email domain part is empty"
        elif "." not in email_domain_part:
            return False, "user email domain must contain dot"
        else:
            return True, "user email is valid"


def is_active_valid_checker(user: dict) -> tuple[bool, str]:
    is_active_status = user.get("is_active")

    if type(is_active_status) != bool:
        return False, "is_active status is invalid"
    else:
        return True, "is_active status is valid"


def user_data_valid_checker(user_base: list) -> tuple[int, int, list]:
    checked_users = 0
    errors_counter = 0
    data_validation_errors = []

    for user in user_base:
        checked_users += 1

        if user.get("id") == None:
            user_name = f"User {user.get('name')}"
        else:
            user_name = f"User {user.get('id')}"

        is_id_valid, id_description = id_valid_checker(user)
        is_name_valid, name_description = name_valid_checker(user)
        is_email_valid, email_description = email_valid_checker(user)
        is_active_status, is_active_description = is_active_valid_checker(user)

        if not is_id_valid:
            errors_counter += 1
            id_error = {}
            id_error["user_id"] = user_name
            id_error["error"] = id_description
            data_validation_errors.append(id_error)

        if not is_name_valid:
            errors_counter += 1
            name_error = {}
            name_error["user_id"] = user_name
            name_error["error"] = name_description
            data_validation_errors.append(name_error)

        if not is_email_valid:
            errors_counter += 1
            email_error = {}
            email_error["user_id"] = user_name
            email_error["error"] = email_description
            data_validation_errors.append(email_error)

        if not is_active_status:
            errors_counter += 1
            is_active_error = {}
            is_active_error["user_id"] = user_name
            is_active_error["error"] = is_active_description
            data_validation_errors.append(is_active_error)

    return checked_users, errors_counter, data_validation_errors


checked_users, errors_counter, data_validation_errors = user_data_valid_checker(users)

print(f"Checked users: {checked_users}")
print(f"Errors found: {errors_counter}")
print()
print("Errors:")

for error in data_validation_errors:
    print(f"{error.get('user_id')}: {error.get('error')}")

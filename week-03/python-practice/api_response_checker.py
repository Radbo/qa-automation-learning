import requests

url = "https://jsonplaceholder.typicode.com/users"


def api_response(url: str) -> tuple[int, list, type]:
    response = requests.get(url)
    response_code = response.status_code
    response_content_json = response.json()
    response_type = type(response_content_json)
    return response_code, response_content_json, response_type


def user_id_checker(user: dict) -> tuple[bool, str]:
    user_id = user.get("id")

    if user_id == None:
        return False, "id is missing"
    elif type(user_id) != int:
        return False, "id is not integer"
    elif user_id <= 0:
        return False, "id must be greater than 0"
    else:
        return True, "user id is valid"


def user_name_checker(user: dict) -> tuple[bool, str]:
    user_name = user.get("name")

    if user_name == None:
        return False, "user name is missing"
    elif not user_name:
        return False, "user name is empty"
    elif type(user_name) != str:
        return False, "user name is not string"
    else:
        return True, "user name is valid"


def username_checker(user: dict) -> tuple[bool, str]:
    username = user.get("username")

    if username == None:
        return False, "username is missing"
    elif not username:
        return False, "username is empty"
    elif type(username) != str:
        return False, "username is not string"
    else:
        return True, "username is valid"


def user_email_checker(user: dict) -> tuple[bool, str]:
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


def user_data_valid_checker(users: list) -> tuple[int, int, list]:
    checked_users = len(users)
    errors = []

    for user in users:
        
        if user.get("id") == None:
            user_id = f"User {user.get('name')}"
        else:
            user_id = f"User {user.get('id')}"
        
        id_valid_status, id_valid_description = user_id_checker(user)
        name_valid_status, name_valid_description = user_name_checker(user)
        username_valid_status, username_valid_description = username_checker(user)
        email_valid_status, email_valid_description = user_email_checker(user)

        if not id_valid_status:
            id_error = {}
            id_error["user_id"] = user_id
            id_error["error"] = id_valid_description
            errors.append(id_error)

        if not name_valid_status:
            name_error = {}
            name_error["user_id"] = user_id
            name_error["error"] = name_valid_description
            errors.append(name_error)

        if not username_valid_status:
            username_error = {}
            username_error["user_id"] = user_id
            username_error["error"] = username_valid_description
            errors.append(username_error)

        if not email_valid_status:
            email_error = {}
            email_error["user_id"] = user_id
            email_error["error"] = email_valid_description
            errors.append(email_error)

    return checked_users, len(errors), errors


def print_report(*, response_code: int, response_type: type, checked_users: int, errors_counted: int, errors_list: list):
    print("API Response Checker\n")
    print(f"Status code: {response_code}")
    print(f"Response type: {response_type}")
    print(f"Checked users: {checked_users}")
    print(f"Errors found: {errors_counted}")
    print("\nErrors:")
    
    if len(errors_list) == 0:
        print("No errors found")
    else:
        for error in errors_list:
            print(f"{error.get('user_id')}: {error.get('error')}")


api_response_code, api_response_content_json, api_response_type = api_response(url)

if api_response_code != 200:
    print(f"api response code is {api_response_code}")
elif api_response_type != list:
    print("Incorrect api response type")
elif not api_response_content_json:
    print("No users found")
else: 
    checked_users, errors_counter, errors_list = user_data_valid_checker(api_response_content_json)
    print_report(response_code=api_response_code, response_type=api_response_type, checked_users=checked_users, errors_counted=errors_counter, errors_list=errors_list)
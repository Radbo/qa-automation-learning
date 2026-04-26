# Task 1
user1 = {"name": "Anna", "age": 25, "city": "Moscow"}
user2 = {"city": "Moscow", "name": "Anna", "age": 25}

print(f"Is user1 and user2 equal: {user1 == user2}")

# Task 2
profile1 = {"name": "Sam", "email": "sam@mail.ru", "active": True}
profile2 = {"name": "Sam", "email": "sam@mail.ru", "active": False}

print(f"Is profile1 and profile2 equal: {profile1 == profile2}")

# Task 3
default_settings = {"theme": "light", "language": "ru", "notifications": True}
user_settings = {"language": "ru", "notifications": True, "theme": "light"}

print(f"Is default settings and user settings equal: {default_settings == user_settings}")

# Task 4
target_product = {"title": "Book", "price": 500, "in_stock": True}

products = [
    {"title": "Pen", "price": 50, "in_stock": True},
    {"title": "Book", "price": 500, "in_stock": True},
    {"title": "Book", "price": 600, "in_stock": True}
]

print(target_product in products)

# Task 5
dict1 = {"age": 20}
dict2 = {"age": "20"}
# dict1 not equal for dict2 besause they have different types (int and str)

# Task 6
student1 = {"name": "Олег", "grades": [5, 4, 5]}
student2 = {"grades": [5, 5, 4], "name": "Олег"}

print(f"Is student1 and student2 equal data: {student1 == student2}")

# Task 7
a = {"x": 10, "y": 20}
b = {"y": 20, "x": 10}

def are_same(a: dict, b: dict) -> bool:
    return a == b

result_are_same = are_same(a, b)
print(f"Result are_same function: {result_are_same}")

# Task 8
person = {"name": "Mary", "age": 30}
additional_info = {"city": "Paris", "job": "designer"}

person.update(additional_info)

print(f"Dict after .update(): {person}")

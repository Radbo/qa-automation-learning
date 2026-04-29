def sort_by_len(element: str) -> int:
    return len(element)

fruits = ["banana", "apple", "cherry", "watermelon", "mango"]

sorted_fruits = sorted(fruits, key=sort_by_len)

print(sorted_fruits)


people = [
    {"name": "Alice", "age": 25},
    {"name": "Max", "age": 38},
    {"name": "Tony", "age": 50},
    {"name": "Rob", "age": 50},
    {"name": "Anna", "age": 38}
]

def sort_by_age_name(people: dict) -> tuple[int, str]:
    return people["age"], people["name"]

sorted_people = sorted(people, key=sort_by_age_name)

print(sorted_people)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_numbers_filter(number: int) -> bool:
    return number % 2 == 0

numbers_filter = list(filter(even_numbers_filter, numbers))

print(numbers_filter)
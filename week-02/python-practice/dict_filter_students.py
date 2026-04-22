students = {
    "Anna": 85,
    "John": 40,
    "Mike": 70
}

for name, points in students.items():
    if points > 60:
        print(f"{name}: {points}")
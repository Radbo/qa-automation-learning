# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# person["job"] = "driver"

# print(person)

# print(person["name"])

# print(person.get("name"))

# for p in person:
#     print(person[p])

# for item in person.items():
#     print(item)

# for key, value in person.items():
#     print(key, value)

# for key in person.keys():
#     print(key)

# for value in person.values():
#     print(value)

person = {
    "city": "New York",
    "age": 30,
    "name": "John"
}

addiional_personal_info = {
    "job": "engeneer",
    "married": True,
    "city": "London"
}

# person.update(addiional_personal_info)

person = person | addiional_personal_info

print(person)


# def add(x: int, y: int):
#     return x + y

# def add_all(*args):
#     summary = 0
#     for num in args:
#         summary += num
    
#     return summary


# print(add_all(1, 2, 3))

def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified

product = {'id': 1, 'name': 'Laptop', 'price': 999.99}

structure = modify_dict(old_dict=product, in_stock=True)

print(type(structure))
print(structure)
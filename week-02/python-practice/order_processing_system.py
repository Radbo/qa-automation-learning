orders = [
    ("apple", 2),
    ("banana", 3),
    ("apple", 1),
    ("orange", 5),
    ("banana", 2)
]

product_order = {}

for product, piece in orders:
    if product in product_order:
        product_order[product] += piece
    else:
        product_order[product] = piece

most_product = max(product_order, key=product_order.get)

print(f"Most popular product: {most_product}")

for product, piece in product_order.items():
    print(f"{product}: {piece}")

prices = {
    "apple": 10,
    "banana": 5,
    "orange": 7
}

total_order_amount = 0

for product, piece in product_order.items():
    total_order_amount += piece * prices[product]

print(total_order_amount)
# Task 1
numbers = [1, 2, 3, 4, 5]
print(f"First number in list - {numbers[0]}, last number in list - {numbers[-1]}")
print(f"Length of this list - {len(numbers)} numbers")
if 10 in numbers:
    print("This list contains number 10")
else:
    print("This list have no number 10")


# Task 2
new_numbers = [1, 2, 3]
new_numbers.append(4)
new_numbers.pop()
new_numbers.reverse()
print(new_numbers)

# Task 3
text = "apple banana orange"
text_list = text.split()
text_list_reversed = text_list[::-1]
text_list_reversed = "-".join(text_list_reversed)
print(text_list_reversed)
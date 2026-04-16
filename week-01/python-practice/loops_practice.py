file_names = ["file1.txt", "image.png", "document.pdf", "notes.txt", "presentation.pptx"]

for file_name in file_names:
    print(file_name)

greeting = "Hello, World!"
for char in greeting:
    print(char)

user_number = int(input("Enter a number: "))
for number in range(1, user_number + 1):
    print(number)

my_numbers = list(range(10, -1, -1))
print(my_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    numbers[i] += 1
print(numbers)
    
greeting = "Hello, World!"
greeting_list = list(greeting)
for i in range(len(greeting_list)):
    if greeting_list[i] == "o":
        print(i)

# Task 1 - print all the numbers in order up to the number n
user_number = int(input("Please, enter a number: "))
print("Numbers in order, up to and including your number: ", end="")
for number in range(1, user_number + 1):
    print(number, end="")
print()

# Task 2 - print all even numbers in order up to the number n
print("Only even numbers in order, up to and including your number: ", end="")
for number in range(1, user_number + 1):
    if number % 2 == 0:
        print(number, "", end="")
print()

# Task 3 - sum of numbers up to number n
print("The sum of the numbers in order, up to and including your number: ", end="")
for number in range(1, user_number + 1):
    if number == user_number:
        print(f"{number} ", end="")
    else:  
        print(f"{number} + ", end="")
print(f"= {sum(list(range(1, user_number + 1)))}")

# Task 4 - щutput only words longer than 5 characters
fruits = ["apple", "banana", "kiwi", "pear", "watermelon"]
for word in fruits:
    if len(word) > 5:
        print(word)

# Task 5 - character counter
greeting_text = "hello world python"
count_o = 0
for char in greeting_text:
    if char == "o" or char == "O":
        count_o += 1
print(count_o)

# Task 6 - split and loop
products = "milk, bread, eggs, cheese"
products_list = products.split(",")
clean_products_list = [item.strip() for item in products_list]
for item in clean_products_list:
    print(f"- {item}")

# Task 7 - multiplication table up to 3 × 4
for first_number in range(1, 4):
    for second_number in range(1, 5):
        print(f"{first_number * second_number}  ", end="")
    print()

# Task 8 - print a rectangle with a given width and height
rectangle_width = 5
rectangle_height = 3
for item_1 in range(1, rectangle_height + 1):
    for item_2 in range(1, rectangle_width + 1):
        print("*", end="")
    print()
    
# Task 9 - print a triangle with a given height
triangle_height = 4
triangle_width = 0
for star_1 in range(1, triangle_height + 1):
    triangle_width += 1
    for star_2 in range(1, triangle_width + 1):
        print(f"*", end="")
    print()
    
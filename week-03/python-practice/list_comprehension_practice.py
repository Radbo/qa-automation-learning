squares = []

for number in range (1, 10):
    squares.append(number **2)

squares_short = [number **2 for number in range(1, 10)]

even_squares = []

for number in range (1, 10):
    if number % 2 == 0:
        even_squares.append(number **2)

short_even_squares = [number **2 for number in range (1, 10) if number % 2 == 0]

even_and_odd = ["odd" if number % 2 == 1 else "even" for number in range(1,10)]

square_dict = {x: x ** 2 for x in range(1,10)}

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
 

print(squares)
print(squares_short)

print(even_squares)
print(short_even_squares )
print(even_and_odd)
print(square_dict)
print(transpose_matrix)
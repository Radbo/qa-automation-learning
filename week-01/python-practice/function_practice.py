numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8]
numbers_2 = [1, 2, 3, 4, 5]


def find_average(numbers):
    average = sum(numbers) // len(numbers)
    return average



def count_vowels(string):
    VOWELS = "aeiouAEIOU"
    count = 0
    for char in string:
         if char in VOWELS:
             count += 1
    
    return count


greetings_string = "Hellow, world"
print(count_vowels(greetings_string))


def formate_date(*, day: int, month: str) -> str:
    return f"Today {day} {month}"

print(formate_date(day=15, month="October"))
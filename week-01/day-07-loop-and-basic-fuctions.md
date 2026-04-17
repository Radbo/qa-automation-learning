# Day 07 — Loops and basic functions

Date: April 16, 2026

Today I continued studying Python fundamentals and focused on loops (`for`) and basic functions.

This was my first day working with iteration and repeated execution of code, which is a key concept in programming.

## Loops (`for`)

Learned how `for` loops work in Python.

A loop allows executing a block of code multiple times.

Basic example:

```python
for item in items_list:
    print(item)
```

Key ideas:

- `item` is a temporary variable that represents each element
- the loop goes through all elements one by one
- for strings, iteration happens character by character

## `range()` function

Learned how to generate sequences of numbers using `range()`.

### Forms of `range()`

- `range(stop)` → from `0` to `stop - 1`
- `range(start, stop)` → from `start` to `stop - 1`
- `range(start, stop, step)` → custom step

Examples:

```python
range(4)        # 0, 1, 2, 3
range(1, 4)     # 1, 2, 3
range(1, 10, 2) # 1, 3, 5, 7, 9
```

Also used:

```python
list(range(5))
```

## Accumulator operators

Learned how to update variables:

- `+=`
- `-=`
- `*=`

Example:

```python
count += 1
```

## `continue`

Learned how to skip the current iteration:

```python
for number in range(10):
    if number == 5:
        continue
    print(number)
```

## Nested loops

Practiced nested loops (loop inside another loop).

Used them to:

- print multiplication tables
- draw shapes using `*`

Example:

```python
for i in range(3):
    for j in range(5):
        print("*", end="")
    print()
```

Also implemented a multiplication table:



## Practical tasks

Completed multiple exercises to reinforce loops:

- iterating through lists and strings
- printing numbers in range
- filtering values (even numbers, long words)
- counting characters in a string
- splitting and processing text
- generating shapes (rectangle, triangle)
- building simple multiplication tables

Main practice file:



## Functions

Started working with functions.

Learned:

- how to define functions using `def`
- how to return values using `return`
- basic type annotations

Example:

```python
def formate_date(*, day: int, month: str) -> str:
    return f"Today {day} {month}"
```

Practice file:



Also implemented:

- average calculation
- vowel counting function

## Code principles

Learned about:

- DRY (Don't Repeat Yourself)
- using `pass` as a placeholder in functions

## Challenges

- still learning how to format output nicely (alignment in tables)
- need more practice with loops and combining logic
- functions are still simple and not deeply used yet

## Result of the day

- understood how loops work
- practiced iteration over different data types
- learned how to use `range()`
- wrote multiple loop-based exercises
- started using functions with return values
- improved confidence writing longer code blocks

## Plan for tomorrow

- continue practicing loops (more complex tasks)
- write more functions
- start combining loops + functions
- improve code readability and structure


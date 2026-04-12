# Day 04 — Boolean logic and conditional statements
Date: April 12, 2026

Today I continued studying Python fundamentals and focused on boolean logic, comparison operators, and conditional statements.

## Boolean values

Learned how boolean values work in Python.

- `True`
- `False`

Boolean values are often produced by comparison operations.

Example:

```python
5 > 3
```

This expression returns `True`.

## Comparison operators

Studied the main comparison operators in Python:

* `==` — equality comparison
* `!=` — not equal
* `>` — greater than
* `<` — less than
* `>=` — greater or equal
* `<=` — less or equal

The result of a comparison can be stored in a variable.

Example:

```python
result = 10 > 5
```

## Logical operators

Learned how to combine multiple conditions.

* `and` — all conditions must be true
* `or` — at least one condition must be true
* `not` — inverts a boolean value

Example:

```python
age > 18 and has_ticket
```

## Bool function

Learned how the `bool()` function evaluates values.

Examples:

```python
bool(-1)  # True
bool(0)   # False
bool(1)   # True
```

Strings also follow this rule:

```python
bool("")      # False
bool("text")  # True
```

Empty values evaluate to `False`.

## Conditional statements

Studied how conditional logic works.

```python
if condition:
    do_something()
```

Important rules:

* blocks are defined by indentation
* Python typically uses **4 spaces**

### if / elif / else

* `if` — first condition
* `elif` — additional mutually exclusive conditions
* `else` — fallback when no condition is met

Example structure:

```python
if condition1:
    ...
elif condition2:
    ...
else:
    ...
```

Also learned the difference between:

* multiple `if` statements (several conditions may run)
* `elif` chain (only one condition executes)

## Strings

Studied basic operations with strings.

Strings can be declared using:

```
"double quotes"
'single quotes'
```

For multiline text:

```python
text = """
large
multi-line
text
"""
```

### Useful string functions and methods

* `len()` — length of a string
* `type()` — check variable type
* `.upper()` — uppercase
* `.lower()` — lowercase
* `.strip()` — remove outer spaces
* `.replace()` — replace text
* `.count()` — count substring
* `.isdigit()` — check if string contains digits
* `in` — check substring presence

Example:

```python
"cat" in "concatenate"
```

## Practice tasks

### 1. Building task improvement

Improved the apartment calculation program.

The program now:

* checks that the apartment number is between **1 and 100**
* prints an error message if the number is outside the range

Example message:

```
Please, enter flat number from 1 to 100
```

Also improved the formatting of the output messages.

I also started adding validation for incorrect user input such as:

* text
* empty input
* spaces

### 2. Leap year task

Solved a small exercise to determine whether a year is a leap year.

This exercise helped practice:

* `if`
* `elif`
* `else`
* `%` operator
* comparison operators

The task was relatively simple, but it helped reinforce conditional logic.

## Code improvements

Continued improving the program in:

`building_task.py`

The program now attempts to detect:

* numbers
* text input
* empty input

Future improvement planned:

* handle negative numbers correctly
* improve input validation logic

## Result of the day

* better understanding of boolean logic
* learned how conditional statements work
* practiced logical operators
* improved my first Python program with input validation
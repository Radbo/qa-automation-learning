# Day 06 — String formatting and list basics
Date: April 15, 2026

Today I continued studying Python fundamentals and learned more about string formatting and list operations.

## String formatting

Learned different ways to insert variables into text output.

### f-strings

Studied f-strings as a modern and convenient way to place variables inside a string.

Example:

```python
print(f"Hello, my name is {name}, my age is {age}")
```

### `str.format()` method

Learned how to format strings using the `format()` method.

Example:

```python
print("Hello, my name is {}, my age is {}".format(name, age))
```

### Percent formatting

Also learned the older percent formatting style.

Example:

```python
print("Hello, my name is %s, my age is %d" % (name, age))
```

## Lists

Started learning lists in Python.

A list is a data structure used to store ordered values.

Example:

```python
my_list = [1, 2, 3]
```

Also learned that lists can contain different data types, although in practice it is usually better to keep them consistent.

## Creating lists

Learned different ways to create lists.

```python
numbers = [1, 2, 3]
words = list(("a", "b", "c"))
```

## Working with lists

### Length of a list

Used the built-in `len()` function to find the number of elements in a list.

```python
len(my_list)
```

### Boolean value of lists

Learned that:

- an empty list is `False`
- a non-empty list is `True`

### Membership check

Learned how to check whether a value exists in a list.

```python
"apple" in my_list
```

### Comparing lists

Learned that two lists are equal only if they contain the same elements in the same order.

```python
list_1 == list_2
```

### Concatenation

Learned that lists can be joined together with `+`.

```python
list_1 + list_2
```

## List methods

Studied several important list methods.

### `.append()`

Adds one element to the end of the list.

```python
my_list.append(value)
```

### `.pop()`

Removes and returns the last element by default.

```python
last_item = my_list.pop()
```

### `.extend()`

Adds all elements from another iterable to the list.

```python
my_list.extend(other_list)
```

### `.reverse()`

Reverses the order of the list in place.

```python
my_list.reverse()
```

### `.sort()`

Sorts the list in ascending order.

```python
my_list.sort()
```

To sort in descending order:

```python
my_list.sort(reverse=True)
```

## String and list conversion

### `.split()`

Learned how to split a string into a list.

```python
text.split(", ")
```

### `.join()`

Learned how to join list elements into a string.

```python
", ".join(my_list)
```

## Built-in functions for lists

Learned how to use:

- `max()`
- `min()`
- `sum()`

## Indexes and slicing

Learned that list elements can be accessed by index.

- positive indexes start from `0`
- negative indexes start from `-1`

Examples:

```python
my_list[0]
my_list[-1]
```

Also learned that list elements can be changed by index.

```python
my_list[1] = "new value"
```

### Slicing

Practiced slicing lists.

```python
my_list[0:5]
my_list[0:10:2]
my_list[::2]
```

## Slicing strings

Also learned that slicing works with strings.

```python
text[5:]
text[::2]
```

## Reversing a list

Learned three ways to reverse a list:

```python
my_list[::-1]
my_list.reverse()
list(reversed(my_list))
```

## Practice tasks

Completed several small practical exercises on list operations.

Files completed today:

- `list_practice.py`
- `shopping_list_manager.py`

## Result of the day

- learned modern and older ways of string formatting
- understood how lists are created and used
- practiced list methods
- learned indexing and slicing
- completed first practical tasks with lists
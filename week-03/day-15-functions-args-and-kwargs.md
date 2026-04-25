# Day 15 — Functions: *args and **kwargs

Date: April 25, 2026

Today I continued learning Python functions and focused on working with variable arguments.

## Functions and arguments

- learned how to use `*args` to pass a variable number of positional arguments
- understood that `args` is stored as a tuple
- practiced iterating through `args` to calculate a result (sum of numbers)

## Unpacking arguments

- learned how to unpack lists using `*` when passing them into functions
- understood how functions can accept multiple values dynamically

## Keyword arguments

- learned how to use `**kwargs` for named arguments
- understood that `kwargs` is stored as a dictionary
- practiced iterating through key-value pairs

## Practical task

Implemented a function:

- `modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]`

Function behavior:

- updates dictionary values if they differ
- returns:
  - modified dictionary
  - boolean flag indicating whether changes were made

## Example

```
product = {'id': 1, 'name': 'Laptop', 'price': 999.99}

structure = modify_dict(old_dict=product, in_stock=True)
```

## What I practiced

- working with `*args` and `**kwargs`
- dictionary manipulation
- conditional updates
- returning multiple values from a function
- basic function design

## Key understanding

- `*args` → flexible positional input (tuple)
- `**kwargs` → flexible named input (dict)
- functions can be designed to be dynamic and reusable
- returning `(result, status)` is a useful pattern for real applications
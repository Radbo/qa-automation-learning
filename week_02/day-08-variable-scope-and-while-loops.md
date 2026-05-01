# Day 08 — Variable scope and while loops  

Date: April 17, 2026

Today I continued studying Python fundamentals and focused on variable scope and `while` loops.

## Variable scope

Learned how variable scope works in Python.

Key ideas:

- variables created inside a function exist only within that function (local scope)
- they cannot be accessed outside of the function

Example concept:

```python
def my_function():
    local_var = 10
```

`local_var` exists only inside the function.

### Global vs local variables

Learned that:

- variables defined outside a function are global
- they can be accessed inside a function

However:

- if a variable is reassigned inside a function, it becomes a new local variable
- even if it has the same name as a global variable

This means:

- the global and local variables can have the same name
- but they store different values

Important note:

- global variables can be modified using `global`
- but this is not recommended practice and should be avoided when possible

## While loop

Studied the `while` loop.

Key difference from `for` loop:

- `for` loop → used when the number of iterations is known
- `while` loop → used when the number of iterations is unknown

The loop runs while a condition is `True`.

Example:

```
while condition:
    do_something()
```

### Common use cases

- counting with a condition
- processing data until a condition changes
- removing elements from a list

Example idea:

```
while my_list:
    my_list.pop()
```

### Infinite loops

Learned that:

- `while` loop can become infinite if the condition never becomes `False`
- it can be stopped manually or using `break`

## Practice

Today I created and worked on the following files:

- `variable_scope_practice.py` — practice with local and global variables 
- `while_loop_practice.py` — practice with `while` loops and different use cases 
- `martingale_heads_and_tails.py` — simulation of the martingale betting strategy using functions and loops 

The martingale program helped me practice:

- functions
- `if` conditions
- `for` and `while` loops
- variable scope
- basic simulation logic

## Software testing course

Also started the course:

- Software Testing and Automation Specialization (University of Minnesota)

Completed the first two lessons:

- Introduction to testing 
- Why and how we test 

Key ideas learned:

- testing is essential because software always contains bugs
- testing helps detect defects but cannot guarantee their absence
- testing always covers only a small part of all possible system states
- important concepts:
  - verification — are we building the product correctly
  - validation — are we building the right product

## Challenges

- did not spend enough time on coding practice today
- focused more on theory due to starting the testing course

## Result of the day

- understood how variable scope works
- learned how `while` loops operate
- practiced loops and functions in small programs
- wrote a more complex simulation program
- started learning software testing fundamentals

## Plan for tomorrow

- continue the testing course
- focus more on Python practice
- solve multiple small tasks using:
  - `while` loops
  - functions
  - conditions
- start combining all learned concepts into mini-projects
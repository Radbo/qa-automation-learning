# Day 13 — Refactoring and function-based code structure

Date: April 23, 2026

Today I focused on improving code quality by refactoring previously written scripts and converting them into function-based implementations.

## Refactoring approach

The main goal of the day was:

- move from script-style code to structured functions
- separate logic from input/output
- improve readability and reusability
- start thinking in terms of data processing instead of linear execution

------

## Refactored tasks

### 1. Sum of digits

- extracted logic into a reusable function
- added support for negative numbers using `abs()`



------

### 2. Reverse number

- implemented function-based solution
- added handling for negative numbers
- used string slicing for simplification



------

### 3. Digit counter

- moved logic into a function
- normalized input using `abs()`



------

### 4. Tuple element counter

- implemented counting using dictionary aggregation
- used `.get()` for clean accumulation pattern



------

### 5. Pairs to dictionary

- converted list of tuples into dictionary using function



------

### 6. Student filtering

- implemented filtering logic with dictionary iteration
- returned new dictionary with filtered data



------

## Test results analyzer (main focus)

Reworked a complex task into a structured solution using multiple functions.

Implemented:

- `get_failed_tests()`
- `get_passed_tests()`
- `get_longest_test()`
- `total_test_duration()`
- `get_pass_rate()`
- `average_test_duration()`
- `get_slow_tests()`
- `analyze_tests()`

Key improvements:

- separated data processing into independent functions
- avoided monolithic loop logic
- introduced summary dictionary for aggregated results
- added new metrics:
  - pass rate
  - average duration
  - slow tests filtering



------

## What I practiced

- function design and decomposition
- working with tuples and dictionaries in real scenarios
- separating logic from input/output
- using aggregation patterns (`.get()`)
- writing reusable and testable code
- improving naming consistency

------

## Result of the day

- transitioned from script-style code to function-based structure
- improved ability to break problems into smaller logical units
- wrote first structured data-processing module (test analyzer)
- reduced code duplication and improved clarity
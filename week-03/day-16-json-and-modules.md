# Day 16 — JSON and Modules in Python

Date: April 27, 2026

Today I learned how to work with JSON data and how Python modules are structured and used.

## JSON basics

- imported the json module
- learned how to convert Python data to JSON format using `json.dumps()`
- understood that the result of `json.dumps()` is a string
- learned how to parse JSON data using `json.loads()`

Practiced working with JSON in a separate script 

## Modules in Python

- learned that a module is a `.py` file containing code, functions, or classes
- understood that each module has its own namespace
- explored module namespace using `globals()`

## Working with imports

- used `import` to include modules in a file
- learned different import styles:
  - import full module
  - import specific functions
  - avoid `import *` due to name conflicts
- used aliasing with `as` to rename imported functions

Example:

```
from math_operations import add as addition
```

## Built-in modules

- practiced with random module
- used `random.choice()` to select a random element
- explored module functions using `dir()`

Practice file: 

## Additional practice

- worked with dictionary comparisons and operations
- used `.update()` to merge dictionaries
- practiced writing reusable functions

Practice file: 

## Key takeaways

- JSON is essential for working with APIs and data exchange
- modules help structure and reuse code
- understanding imports is critical for larger projects
- namespaces prevent conflicts between functions and variables
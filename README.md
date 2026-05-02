# qa-automation-learning

This repository documents my learning path toward QA Automation.

I use it to practice Python, Git, testing fundamentals, pytest, JSON data validation, API response checking, and project organization.

## Current Progress

I am currently working through the early stage of my QA Automation learning plan.

Completed and practiced so far:

- Python environment setup
- Git and GitHub basics
- Python variables, conditions, loops, functions
- strings, lists, tuples, dictionaries, sets
- JSON basics
- Python modules and imports
- basic `requests` usage
- JSON-like data validation
- API response validation
- basic pytest tests
- running pytest from the repository root

## Project Structure

```text
qa-automation-learning/
├── week-01/
│   ├── day-*.md
│   └── python-practice/
├── week_02/
│   ├── day-*.md
│   ├── python-practice/
│   └── pytest_practice/
├── week-03/
│   ├── day-*.md
│   └── python-practice/
├── requirements.txt
└── README.md
```

## Main Practice Areas

### Week 01

Basic Python and Git practice:

- environment setup
- Git core concepts
- Python basics
- conditions
- loops
- functions
- simple practice scripts

### Week 02

Python core and first testing practice:

- variable scope
- while loops
- tuples
- dictionaries
- data processing
- first mini-projects
- basic pytest tests
- project structure for test execution

### Week 03

Python for QA Automation:

- `*args` and `**kwargs`
- JSON basics
- modules and imports
- `requests`
- sorting and filtering
- JSON-like data validation
- API response checking

## How To Run Tests

Run pytest from the repository root:

```bash
python3 -m pytest
```

Expected current result:

```text
7 passed
```

## How To Run Practice Scripts

Run JSON-like data validation practice:

```bash
python3 week-03/python-practice/json_data_checker.py
```

Run API response checker practice:

```bash
python3 week-03/python-practice/api_response_checker.py
```

## Current API Practice

The API response checker sends a GET request to:

```text
https://jsonplaceholder.typicode.com/users
```

It checks:

- response status code
- response data type
- non-empty response list
- user `id`
- user `name`
- user `username`
- user `email`

Current successful output:

```text
Status code: 200
Response type: <class 'list'>
Checked users: 10
Errors found: 0
No errors found
```

## Learning Goal

The long-term goal of this repository is to build practical QA Automation skills and gradually move toward portfolio-ready projects.

Target skills:

- manual QA fundamentals
- Python for test automation
- pytest
- API testing
- UI automation
- SQL basics
- CI/CD basics
- Docker basics
- clean project documentation

## Notes

This is a learning repository, so some early scripts are intentionally simple and verbose.

The focus is not only on writing code, but also on understanding errors, debugging, documenting progress, and improving the project step by step.

# Day 19 — Pytest project structure and API practice

Date: May 1, 2026

Today I focused on improving the project structure and continued practicing API response validation.

## Pytest structure fix

I fixed the pytest project structure so tests can be started from the repository root.

Previously, tests worked only from the pytest practice folder.
Now tests can be started with one command from the root of the repository.

Command:

python3 -m pytest

Result:

7 passed

## What I practiced

- project structure for pytest
- Python imports
- running tests from the repository root
- organizing test files in a more import-friendly structure

## API response checker practice

I created a simple API response checker.

The script sends a GET request to JSONPlaceholder API and validates user data from the response.

API used:

https://jsonplaceholder.typicode.com/users

Implemented checks:

- status code
- response type
- non-empty response list
- user id
- user name
- username
- user email

## API checker result

The script successfully checked 10 users from the API response.

Final output:

Status code: 200
Response type: <class 'list'>
Checked users: 10
Errors found: 0
No errors found

## Key understanding

Today I practiced moving from static JSON-like data validation to real API response validation.

I understood that before validating API data, it is important to check:

- response status code
- response data type
- whether the response contains expected data

Only after these checks does it make sense to validate individual fields.

## Result

By the end of the day:

- pytest runs successfully from the repository root
- all 7 tests pass
- API response checker works correctly
- user data from API response is validated
- the project became closer to a real QA Automation repository
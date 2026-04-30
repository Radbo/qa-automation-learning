# Day 18 — Project health check and JSON data validation practice

Date: April 30, 2026

Today I focused on improving the technical health of my QA Automation learning project and practiced validating JSON-like user data.

## Project health check

I started the day by checking existing project problems and fixing issues that prevented the code from working correctly.

## Fixed issues

- fixed invalid syntax in JSON practice file
- corrected problems with dictionary keys
- fixed issues caused by missing fields in dictionaries
- practiced reading Python traceback errors
- improved understanding of common Python errors

## Errors I practiced debugging

Today I worked with several real Python errors:

- `KeyError`
- `NameError`
- `TypeError`
- `AttributeError`
- `SyntaxError`

## JSON data validation practice

I created a data validation script for a list of users.

The script checks:

- user id
- user name
- user email
- user active status

## User data checks

For `id` validation I practiced checking:

- missing id
- incorrect id type
- invalid id value

For `name` validation I practiced checking:

- missing name
- empty name
- incorrect name type

For `email` validation I practiced checking:

- missing email
- empty email
- email without `@`
- email with invalid structure
- email without local part
- email without domain part
- email domain without dot

For `is_active` validation I practiced checking:

- missing active status
- incorrect active status type

## What I improved

- learned why direct dictionary access like `user["field"]` can be dangerous
- practiced using `.get()` for safer access to dictionary values
- improved validation logic for incomplete data
- improved error reporting
- learned how to collect multiple validation errors
- made output easier to read

## Key understanding

I understood that external data can be incomplete or invalid.

A validation script should not crash when a field is missing.  
It should detect the problem and report it clearly.

I also understood the difference between:

- checking a value
- checking a type
- checking whether a key exists
- creating a readable validation report

## Result

By the end of the day I created a working JSON-like data checker.

The script checks 20 users, finds validation errors, and prints a readable report.


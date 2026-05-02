# Day 20 — Week 03 review and API checker refactoring

Date: May 2, 2026

Today I focused on reviewing Week 03 progress and improving the API response checker.

## API response checker refactoring

I improved the API response checker script.

What I changed:

- renamed response-related variables
- removed unused import
- fixed function naming
- improved final validation flow
- checked status code before validating response data
- checked response type before looping through users
- checked that response list is not empty

## What I practiced

- working with requests
- using response.json()
- validating API response data
- checking status code
- checking response type
- validating user fields
- printing a readable validation report

## Result

The API response checker works correctly.

Final output:

Status code: 200
Response type: <class 'list'>
Checked users: 10
Errors found: 0
No errors found

## Key understanding

Before validating API response data, it is important to check that the request was successful and that the response has the expected structure.

I also understood that `!=` should be used for value comparison, while `is` and `is not` are mostly used for identity checks such as comparing with `None`.

## Week 03 summary

This week I practiced:

- JSON basics
- Python modules
- requests basics
- API response validation
- data validation
- pytest project structure
- running tests from the repository root

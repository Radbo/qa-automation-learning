# Day 10 — ATM Simulator project

Date: April 19, 2026

Today I focused on completing my first real mini-project — an ATM simulator.

I finalized the implementation, improved structure, and moved the project into a separate repository:
https://github.com/Radbo/atm-simulator

Additionally, I performed manual testing and documented the results.

## What I implemented

- Menu-based CLI application
- Balance checking
- Deposit logic
- Withdraw logic
- Input validation for menu and amounts
- Basic error handling

Core functions:

- `menu_navigation()`
- `integer_input_check()`
- `deposit_maker()`
- `withdraw_maker()`

Example of logic structure:

## What I practiced

- Structuring a program into functions
- Separating validation logic
- Returning multiple values from functions
- Working with global state (and understanding its downsides)
- Building a full user flow (not just isolated tasks)

## Testing

I manually created and executed structured test cases:

### Test Summary

- Total test cases: 35
- Passed: 32
- Failed: 3

### Key issues found

1. Crash on extremely large input values (e.g. `2⁵³`)
2. No handling of leading/trailing spaces
3. No normalization of input

These issues are also documented in README:

## Key result of the day

- First real project completed
- First test documentation written
# Time Calculation in 24-Hour Format

## Goal

Calculate the time after a given number of minutes from a specified starting time in 24-hour format.

## Rules

- The starting time is provided in the format `hh:mm`.
- The number of minutes to add is a non-negative integer.
- The result should also be in `hh:mm` format, with leading zeroes if necessary.

## Input / Output

- **Input**: 
  - A string representing the current time in `hh:mm` format (0 ≤ hh < 24, 0 ≤ mm < 60).
  - An integer `a` (0 ≤ a ≤ 10,000) representing the number of minutes to add.
- **Output**: 
  - A string representing the new time in `hh:mm` format after adding the specified minutes.

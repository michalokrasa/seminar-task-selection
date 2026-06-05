# String Validation

## Goal

Determine if a given string can be constructed by appending 'b's to a string of 'a's, followed by appending 'c's such that the number of 'c's equals the number of 'a's or 'b's.

## Rules

- The string must start with one or more 'a's.
- The 'a's must be followed by one or more 'b's.
- The 'b's must be followed by 'c's.
- The number of 'c's must be equal to the number of 'a's or the number of 'b's.

## Input / Output

- **Input**: A single string `S` consisting only of the characters 'a', 'b', and 'c', with a length between 1 and 5000.
- **Output**: Print "YES" if the string can be constructed as described, otherwise print "NO".

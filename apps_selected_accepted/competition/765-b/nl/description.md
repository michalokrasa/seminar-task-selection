# Obfuscation Check

## Goal

Determine if a given string can be the result of a specific obfuscation process applied to variable names in a program.

## Rules

- The obfuscation process replaces the first unique variable name with 'a', the second with 'b', and so on.
- There are at most 26 unique identifiers in the program.
- The identifiers are replaced in the order they first appear.

## Input / Output

- **Input**: A single string `S` of lowercase English letters (1 ≤ |S| ≤ 500) representing the obfuscated identifiers.
- **Output**: Print "YES" if the string can be a result of the obfuscation process, otherwise print "NO".

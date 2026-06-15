# Predict Child's Choice

## Goal

Determine which choice a child will select based on the length of the descriptions of multiple-choice answers.

## Rules

- Each choice (A, B, C, D) has a description.
- A choice is considered "great" if its description is at least twice as short or twice as long as all other descriptions.
- If exactly one choice is "great," the child selects it.
- If no choice or more than one choice is "great," the child selects choice C.

## Input / Output

- **Input**: Four lines, each starting with "X." (where X is A, B, C, or D), followed by a description of up to 100 characters. The description consists of uppercase/lowercase letters and underscores.
- **Output**: A single character ("A", "B", "C", or "D") representing the child's choice.

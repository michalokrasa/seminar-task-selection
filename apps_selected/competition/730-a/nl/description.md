# Equalize Ratings

## Goal

Determine the maximum possible equal rating for a group of friends by strategically losing matches.

## Rules

- Friends can form a party of 2 to 5 members to lose a match.
- Each losing match decreases the rating of each party member by 1.
- Ratings cannot go below 0.
- The goal is to make all ratings equal and as high as possible.

## Input / Output

- **Input**: 
  - An integer `n` (2 ≤ n ≤ 100) representing the number of friends.
  - A list of `n` non-negative integers representing the initial ratings of the friends, where each rating is between 0 and 100.
  
- **Output**: 
  - An integer `R` representing the final equal rating of all friends.
  - An integer `t` representing the number of matches played.
  - `t` lines, each containing a string of `n` characters ('0' or '1'), indicating which friends participate in each match. Each line must have between 2 and 5 '1's.

# Problem Solving Contest

## Goal

Determine the maximum number of problems Mishka can solve from either end of a list, given his problem-solving skill level.

## Rules

- Mishka can only solve problems from the leftmost or rightmost end of the list.
- Mishka can solve a problem if its difficulty is less than or equal to his skill level, \( k \).
- Once a problem is solved, it is removed from the list.
- Mishka stops solving when he cannot solve any problem from either end.

## Input / Output

- **Input**: 
  - The first line contains two integers \( n \) and \( k \) (\( 1 \le n, k \le 100 \)), representing the number of problems and Mishka's skill level.
  - The second line contains \( n \) integers \( a_1, a_2, \ldots, a_n \) (\( 1 \le a_i \le 100 \)), where each \( a_i \) is the difficulty of the \( i \)-th problem.
  
- **Output**: 
  - Print one integer, the maximum number of problems Mishka can solve.

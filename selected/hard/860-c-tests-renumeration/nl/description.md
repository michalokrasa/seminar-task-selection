# Tests Renumeration

## Goal

Generate a script of `move` commands with the **minimum** number of lines that renames all test files so that example tests are numbered `1` through `e` and regular tests are numbered `e+1` through `n`.

## Rules

- There are `n` test files with arbitrary string names and a type: `1` = example, `0` = regular test.
- The target state: files named `"1"`, `"2"`, …, `"e"` contain examples; files `"e+1"`, …, `"n"` contain regular tests.
- A `move A B` command renames file `A` to `B`; if `B` already exists it is **overwritten**. After the move, `A` no longer exists.
- The script is executed sequentially — each command sees the file system state left by all previous commands.
- Minimise the total number of `move` commands.
- When a target filename collides with a source file that still needs to be moved, use a temporary name to avoid data loss.
- Temporary filenames must be valid (1–6 characters, digits and lowercase letters).

## Input / Output

- **Input**: first line is `n` (1 ≤ n ≤ 10^5); each of the next `n` lines is `name_i type_i`.
- **Output**: first line is the minimum number of moves; the following lines are the move commands.

# Pineapple Barking

## Goal

Determine if a pineapple will bark at a specific time when it barks initially at time `t` and then every `s` seconds twice with a 1-second interval.

## Rules

- The pineapple barks first at time `t`.
- After the first bark, it barks every `s` seconds twice: at `t + s`, `t + s + 1`, `t + 2s`, `t + 2s + 1`, etc.
- Determine if the pineapple will bark at a given time `x`.

## Input / Output

- **Input**: Three integers `t`, `s`, and `x` where `0 ≤ t, x ≤ 10^9` and `2 ≤ s ≤ 10^9`.
- **Output**: Print "YES" if the pineapple will bark at time `x`, otherwise print "NO".

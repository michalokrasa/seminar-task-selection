# Computer Game

## Goal

Determine whether Petya can defeat the boss using his spell scrolls, and if so, find the **minimum time** (in seconds) to do it along with the optimal scroll usage sequence.

## Rules

- The boss starts with `max` HP and regenerates `reg` HP per second (capped at `max`).
- Each second the following occurs in order:
  1. All active spells deal their damage to the boss.
  2. The boss regenerates `reg` HP (total HP cannot exceed `max`).
  3. Petya may use **at most one** scroll (if available and its condition is met).
- A scroll with power `powi` can only be used when the boss's current HP is ≤ `powi`% of `max`.
- Using a scroll activates a permanent spell dealing `dmgi` damage per second from the **next** second onward.
- Second `0` is special: no damage/regen happens, but a scroll may be used (boss starts at `max` HP, so only scrolls with `pow = 100` are usable).
- The boss is defeated when its HP is ≤ 0 at the **end** of a second (after damage and regen).
- Find the minimum time to defeat the boss, or report `NO` if it is impossible.

## Input / Output

- **Input**: first line is `N max reg`; next `N` lines each contain `powi dmgi` (scroll parameters).
- **Output**: `NO` if impossible; otherwise `YES`, then `time num_scrolls`, then `num_scrolls` lines each with `second index` (1-indexed scroll numbers, in usage order).

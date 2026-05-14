# A Good Contest

## Goal

Determine whether Anton had a "good" performance in a rated contest.

## Rules

- A participant's handle is **red** if their rating before the contest was **≥ 2400**.
- Anton's performance is **good** if he outscored at least one participant who:
  1. had a **red** handle before the contest (rating ≥ 2400), **and**
  2. had their rating **increase** after the contest (after > before).
- Both conditions must hold simultaneously for the same participant.

## Input / Output

- **Input**: an integer `n` followed by `n` lines each containing `<handle> <before> <after>`.
- **Output**: `YES` if Anton performed good, `NO` otherwise.

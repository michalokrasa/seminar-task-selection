# Missing Infinity Gems

## Goal

Determine which Infinity Gems are missing from the Gauntlet based on the colors of the Gems present.

## Rules

- There are six Infinity Gems, each associated with a unique color:
  - Power Gem: purple
  - Time Gem: green
  - Space Gem: blue
  - Soul Gem: orange
  - Reality Gem: red
  - Mind Gem: yellow
- You are given the colors of the Gems currently in the Gauntlet.
- Identify the names of the Gems that are absent.

## Input / Output

- **Input**: 
  - The first line contains an integer `n` (0 ≤ n ≤ 6), the number of Gems in the Gauntlet.
  - The next `n` lines each contain a string representing the color of a Gem, chosen from: purple, green, blue, orange, red, yellow.
- **Output**: 
  - The first line should contain an integer `m` (0 ≤ m ≤ 6), the number of absent Gems.
  - The next `m` lines should list the names of the absent Gems, each on a new line, with the first letter uppercase and the rest lowercase. The order of the names does not matter.

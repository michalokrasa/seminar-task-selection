# CF 987/A

## Problem Description
You took a peek on Thanos wearing Infinity Gauntlet. In the Gauntlet there is a place for six Infinity Gems:  the Power Gem of purple color,  the Time Gem of green color,  the Space Gem of blue color,  the Soul Gem of orange color,  the Reality Gem of red color,  the Mind Gem of yellow color. 

Using colors of Gems you saw in the Gauntlet determine the names of absent Gems.


-----Input-----

In the first line of input there is one integer $n$ ($0 \le n \le 6$) — the number of Gems in Infinity Gauntlet.

In next $n$ lines there are colors of Gems you saw. Words used for colors are: purple, green, blue, orange, red, yellow. It is guaranteed that all the colors are distinct. All colors are given in lowercase English letters.


-----Output-----

In the first line output one integer $m$ ($0 \le m \le 6$) — the number of absent Gems.

Then in $m$ lines print the names of absent Gems, each on its own line. Words used for names are: Power, Time, Space, Soul, Reality, Mind. Names can be printed in any order. Keep the first letter uppercase, others lowercase.


-----Examples-----
Input
4
red
purple
yellow
orange

Output
2
Space
Time

Input
0

Output
6
Time
Mind
Soul
Power
Reality
Space



-----Note-----

In the first sample Thanos already has Reality, Power, Mind and Soul Gems, so he needs two more: Time and Space.

In the second sample Thanos doesn't have any Gems, so he needs all six.

## Contest Information
- **URL**: https://codeforces.com/problemset/problem/987/A
- **Difficulty**: interview
- **Tags**: implementation
- **Contest ID**: 987
- **Problem Index**: A
- **Number of Tests**: 64
- **Number of Solutions**: 24

## Task
Solve this competitive programming problem. Write your Python solution to `/app/solution.py`.

Your solution must:
1. Read input from standard input (stdin)
2. Write output to standard output (stdout)
3. Handle all the given constraints and edge cases
4. Be saved to `/app/solution.py`

## Test Cases
The solution will be validated against multiple test cases.

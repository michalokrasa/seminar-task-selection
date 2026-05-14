# 1173_A. Nauuo and Votes

## Problem Description
Nauuo is a girl who loves writing comments.

One day, she posted a comment on Codeforces, wondering whether she would get upvotes or downvotes.

It's known that there were x persons who would upvote, y persons who would downvote, and there were also another z persons who would vote, but you don't know whether they would upvote or downvote. Note that each of the x+y+z people would vote exactly one time.

There are three different results: if there are more people upvote than downvote, the result will be "+"; if there are more people downvote than upvote, the result will be "-"; otherwise the result will be "0".

Because of the z unknown persons, the result may be uncertain (i.e. there are more than one possible results). More formally, the result is uncertain if and only if there exist two different situations of how the z persons vote, that the results are different in the two situations.

Tell Nauuo the result or report that the result is uncertain.

Input

The only line contains three integers x, y, z (0≤ x,y,z≤100), corresponding to the number of persons who would upvote, downvote or unknown.

Output

If there is only one possible result, print the result : "+", "-" or "0".

Otherwise, print "?" to report that the result is uncertain.

Examples

Input


3 7 0


Output


-

Input


2 0 1


Output


+

Input


1 1 0


Output


0

Input


0 0 1


Output


?

Note

In the first example, Nauuo would definitely get three upvotes and seven downvotes, so the only possible result is "-".

In the second example, no matter the person unknown downvotes or upvotes, Nauuo would get more upvotes than downvotes. So the only possible result is "+".

In the third example, Nauuo would definitely get one upvote and one downvote, so the only possible result is "0".

In the fourth example, if the only one person upvoted, the result would be "+", otherwise, the result would be "-". There are two possible results, so the result is uncertain.

## Contest Information
- **Contest ID**: 1173
- **Problem Index**: A
- **Points**: 500.0
- **Rating**: 800
- **Tags**: greedy
- **Time Limit**: {'seconds': 1, 'nanos': 0} seconds
- **Memory Limit**: 256000000 bytes

## Task
Solve this competitive programming problem. Write your Python solution to `/app/solution.py`.

Your solution must:
1. Read input from standard input (stdin)
2. Write output to standard output (stdout)
3. Handle all the given constraints and edge cases
4. Be saved to `/app/solution.py`

## Test Cases
The solution will be validated against multiple test cases.
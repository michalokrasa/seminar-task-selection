# Determine Potential Team Leaders

## Goal

Identify which team members could potentially be the leader based on their presence throughout a recorded segment of an online meeting.

## Rules

- A leader is defined as someone who is present whenever any other team member is present during the meeting segment.
- The meeting segment is represented by a series of log on (`+ id`) and log off (`- id`) messages.
- The sequence of messages is guaranteed to be a correct and continuous part of the meeting.

## Input / Output

- **Input**: 
  - The first line contains two integers, `n` (number of team members) and `m` (number of messages).
  - The next `m` lines each contain a message in the format `+ id` or `- id`, indicating a member logging on or off.
- **Output**: 
  - The first line should contain an integer `k`, the number of potential leaders.
  - The second line should list `k` integers in increasing order, representing the IDs of potential leaders. If no leader is possible, output `0`.

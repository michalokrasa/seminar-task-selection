# Find the Smallest Frame

## Goal

Determine the smallest possible square frame that can encompass all white pixels on a broken monitor screen, where the frame is one pixel wide.

## Rules

- The frame must be a square with a width of 1 pixel.
- The frame should not extend beyond the screen's borders.
- All white pixels must be located on the frame.
- The frame should be the smallest possible size that satisfies the above conditions.
- If multiple frames of the same size exist, any valid frame can be output.
- If no valid frame can be found, output `-1`.

## Input / Output

- **Input**: 
  - The first line contains two integers, `n` and `m` (1 ≤ n, m ≤ 2000), representing the screen's resolution.
  - The next `n` lines each contain `m` characters, either `.` (black pixel) or `w` (white pixel).
  - At least one pixel is guaranteed to be white.

- **Output**: 
  - Print the screen with the frame represented by `+` characters.
  - White pixels (`w`) should remain unchanged.
  - If no valid frame exists, print `-1`.

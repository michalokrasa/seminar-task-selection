import sys
input = sys.stdin.read

def solve():
    data = input().strip().split()
    n = int(data[0])
    m = int(data[1])
    grid = data[2:]
    
    min_row, max_row = n, -1
    min_col, max_col = m, -1
    
    # Find the bounding box of all 'w' pixels
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'w':
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j
    
    # If no 'w' was found, output the grid as is
    if min_row == n:
        for line in grid:
            print(line)
        return
    
    # Calculate the size of the square frame
    side_length = max(max_row - min_row + 1, max_col - min_col + 1)
    
    # Check if the square frame can fit within the grid
    if min_row + side_length > n or min_col + side_length > m:
        print(-1)
        return
    
    # Create a new grid with the frame
    result = [list(row) for row in grid]
    
    for i in range(min_row, min_row + side_length):
        for j in range(min_col, min_col + side_length):
            if result[i][j] == '.':
                result[i][j] = '+'
    
    # Print the result grid
    for line in result:
        print(''.join(line))

solve()
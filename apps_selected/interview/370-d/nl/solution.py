def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    screen = data[1:n+1]
    
    # Find the bounding box of white pixels
    min_row, max_row = n, -1
    min_col, max_col = m, -1
    
    for i in range(n):
        for j in range(m):
            if screen[i][j] == 'w':
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j
    
    # Calculate the size of the square frame
    side_length = max(max_row - min_row + 1, max_col - min_col + 1)
    
    # Check if the square frame can fit within the screen
    if min_row + side_length > n or min_col + side_length > m:
        print(-1)
        return
    
    # Create a new screen with the frame
    result = [list(row) for row in screen]
    
    # Draw the frame
    for i in range(min_row, min_row + side_length):
        result[i][min_col] = '+'
        result[i][min_col + side_length - 1] = '+'
    
    for j in range(min_col, min_col + side_length):
        result[min_row][j] = '+'
        result[min_row + side_length - 1][j] = '+'
    
    # Print the result
    for row in result:
        print(''.join(row))

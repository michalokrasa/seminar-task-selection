def main():
    import sys
    input = sys.stdin.read
    board = input().strip().split()
    
    # Find the minimum distance for a white pawn to reach the first row
    min_white_distance = 8
    for col in range(8):
        for row in range(8):
            if board[row][col] == 'W':
                min_white_distance = min(min_white_distance, row)
                break
    
    # Find the minimum distance for a black pawn to reach the last row
    min_black_distance = 8
    for col in range(8):
        for row in range(7, -1, -1):
            if board[row][col] == 'B':
                min_black_distance = min(min_black_distance, 7 - row)
                break
    
    # Determine the winner
    if min_white_distance <= min_black_distance:
        print('A')
    else:
        print('B')

main()
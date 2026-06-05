def determine_winner(board):
    # Find the minimum row index for a white pawn
    min_white_row = 8
    for col in range(8):
        for row in range(8):
            if board[row][col] == 'W':
                min_white_row = min(min_white_row, row)
                break

    # Find the maximum row index for a black pawn
    max_black_row = -1
    for col in range(8):
        for row in range(7, -1, -1):
            if board[row][col] == 'B':
                max_black_row = max(max_black_row, row)
                break

    # Determine the winner
    if min_white_row <= 7 - max_black_row:
        return 'A'
    else:
        return 'B'

import sys
input = sys.stdin.read
data = input().strip().split()
board = [list(row) for row in data]
print(determine_winner(board))
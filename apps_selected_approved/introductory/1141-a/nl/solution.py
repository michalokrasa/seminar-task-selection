def game_23_transformation(n, m):
    if m % n != 0:
        return -1
    
    quotient = m // n
    moves = 0
    
    while quotient % 2 == 0:
        quotient //= 2
        moves += 1
    
    while quotient % 3 == 0:
        quotient //= 3
        moves += 1
    
    if quotient != 1:
        return -1
    
    return moves

import sys
input = sys.stdin.read
n, m = map(int, input().strip().split())
print(game_23_transformation(n, m))
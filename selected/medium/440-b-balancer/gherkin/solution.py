def minimum_moves_to_equalize(n, boxes):
    target = sum(boxes) // n
    moves = 0
    current_balance = 0
    
    for box in boxes:
        current_balance += box - target
        moves += abs(current_balance)
    
    return moves

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    boxes = list(map(int, data[1:]))
    print(minimum_moves_to_equalize(n, boxes))
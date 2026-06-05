def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    numbers = list(map(int, data[1:]))
    
    from collections import Counter
    count = Counter(numbers)
    
    # Determine the number of elements needed for each type of symmetry
    num_4 = (n // 2) * (n // 2)
    num_2 = (n % 2) * (n // 2) * 2
    num_1 = (n % 2) * (n % 2)
    
    # Prepare lists to store numbers for each type of symmetry
    four_blocks = []
    two_blocks = []
    one_blocks = []
    
    # Try to fill the blocks
    for num, cnt in count.items():
        while cnt >= 4 and len(four_blocks) < num_4:
            four_blocks.append(num)
            cnt -= 4
        while cnt >= 2 and len(two_blocks) < num_2:
            two_blocks.append(num)
            cnt -= 2
        while cnt >= 1 and len(one_blocks) < num_1:
            one_blocks.append(num)
            cnt -= 1
    
    # Check if we have enough numbers for each block
    if len(four_blocks) != num_4 or len(two_blocks) != num_2 or len(one_blocks) != num_1:
        print("NO")
        return
    
    # Create the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the 4-blocks
    idx = 0
    for i in range(n // 2):
        for j in range(n // 2):
            matrix[i][j] = four_blocks[idx]
            matrix[i][n - j - 1] = four_blocks[idx]
            matrix[n - i - 1][j] = four_blocks[idx]
            matrix[n - i - 1][n - j - 1] = four_blocks[idx]
            idx += 1
    
    # Fill the 2-blocks
    idx = 0
    if n % 2 == 1:
        for i in range(n // 2):
            matrix[i][n // 2] = two_blocks[idx]
            matrix[n - i - 1][n // 2] = two_blocks[idx]
            idx += 1
        for j in range(n // 2):
            matrix[n // 2][j] = two_blocks[idx]
            matrix[n // 2][n - j - 1] = two_blocks[idx]
            idx += 1
    
    # Fill the 1-block
    if n % 2 == 1:
        matrix[n // 2][n // 2] = one_blocks[0]
    
    # Output the result
    print("YES")
    for row in matrix:
        print(" ".join(map(str, row)))

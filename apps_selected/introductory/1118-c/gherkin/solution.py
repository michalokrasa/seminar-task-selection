import sys
from collections import Counter

def construct_palindromic_matrix(n, numbers):
    count = Counter(numbers)
    
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Determine the number of 4-corners, 2-edges, and 1-center elements needed
    num_4_corners = (n // 2) * (n // 2)
    num_2_edges = (n % 2) * (n // 2) * 2
    num_1_center = (n % 2) * (n % 2)
    
    # Prepare lists to store elements for each type
    corners = []
    edges = []
    center = []
    
    # Fill corners, edges, and center
    for num, cnt in count.items():
        while cnt >= 4 and len(corners) < num_4_corners:
            corners.append(num)
            cnt -= 4
        while cnt >= 2 and len(edges) < num_2_edges:
            edges.append(num)
            cnt -= 2
        if cnt >= 1 and len(center) < num_1_center:
            center.append(num)
            cnt -= 1
        count[num] = cnt
    
    # Check if we have enough elements to fill the matrix
    if len(corners) != num_4_corners or len(edges) != num_2_edges or len(center) != num_1_center:
        return "NO"
    
    # Fill the matrix with corners
    idx = 0
    for i in range(n // 2):
        for j in range(n // 2):
            matrix[i][j] = matrix[i][n - j - 1] = matrix[n - i - 1][j] = matrix[n - i - 1][n - j - 1] = corners[idx]
            idx += 1
    
    # Fill the matrix with edges
    idx = 0
    if n % 2 == 1:
        for i in range(n // 2):
            matrix[i][n // 2] = matrix[n - i - 1][n // 2] = edges[idx]
            idx += 1
        for j in range(n // 2):
            matrix[n // 2][j] = matrix[n // 2][n - j - 1] = edges[idx]
            idx += 1
    
    # Fill the center
    if n % 2 == 1:
        matrix[n // 2][n // 2] = center[0]
    
    # Return the result
    result = "YES\n"
    for row in matrix:
        result += " ".join(map(str, row)) + "\n"
    return result.strip()

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    numbers = list(map(int, data[1:]))
    
    result = construct_palindromic_matrix(n, numbers)
    print(result)

main()
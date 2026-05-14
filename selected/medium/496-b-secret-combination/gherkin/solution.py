def find_minimum_combination(n, digits):
    def add_one(d):
        return [(int(c) + d) % 10 for c in digits]

    def rotate_right(lst):
        return lst[-1:] + lst[:-1]

    min_combination = digits
    for add_shift in range(10):
        current_digits = add_one(add_shift)
        for _ in range(n):
            current_digits = rotate_right(current_digits)
            current_str = ''.join(map(str, current_digits))
            if current_str < min_combination:
                min_combination = current_str

    return min_combination

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    digits = data[1]
    print(find_minimum_combination(n, digits))
def find_shortest_unique_substrings(phone_numbers):
    n = len(phone_numbers)
    results = [''] * n

    # Function to check if a substring is unique for a given index
    def is_unique(substring, index):
        for i in range(n):
            if i != index and substring in phone_numbers[i]:
                return False
        return True

    # Iterate over each phone number
    for i in range(n):
        number = phone_numbers[i]
        length = len(number)
        found = False

        # Try all possible substring lengths starting from 1
        for l in range(1, length + 1):
            if found:
                break
            # Try all possible substrings of length l
            for start in range(length - l + 1):
                substring = number[start:start + l]
                if is_unique(substring, i):
                    results[i] = substring
                    found = True
                    break

    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    phone_numbers = data[1:n+1]
    results = find_shortest_unique_substrings(phone_numbers)
    for result in results:
        print(result)
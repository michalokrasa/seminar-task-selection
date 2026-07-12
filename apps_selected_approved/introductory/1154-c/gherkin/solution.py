def max_days(a, b, c):
    # The sequence of food consumption over a week
    week_pattern = [0, 1, 2, 0, 2, 1, 0]  # 0: fish, 1: rabbit, 2: chicken

    # Function to calculate how many days we can feed the cat starting from a specific day
    def days_from_start(start_day, a, b, c):
        days = 0
        while True:
            day_type = week_pattern[(start_day + days) % 7]
            if day_type == 0:
                if a > 0:
                    a -= 1
                else:
                    break
            elif day_type == 1:
                if b > 0:
                    b -= 1
                else:
                    break
            elif day_type == 2:
                if c > 0:
                    c -= 1
                else:
                    break
            days += 1
        return days

    # Try starting from each day of the week and find the maximum days
    max_days = 0
    for start_day in range(7):
        max_days = max(max_days, days_from_start(start_day, a, b, c))

    return max_days

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    a, b, c = map(int, data)
    print(max_days(a, b, c))
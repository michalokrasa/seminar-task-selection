def max_days_of_feeding(a, b, c):
    # Days of the week: 0=Monday, 1=Tuesday, ..., 6=Sunday
    # Food requirements: 0, 3, 6 -> Fish; 1, 4 -> Rabbit; 2, 5 -> Chicken
    week_pattern = [0, 1, 2, 0, 1, 2, 0]  # 0=Fish, 1=Rabbit, 2=Chicken
    food_needs = [a, b, c]
    
    # Calculate full weeks that can be fed
    full_weeks = min(a // 3, b // 2, c // 2)
    max_days = full_weeks * 7
    
    # Remaining food after full weeks
    remaining_food = [a - full_weeks * 3, b - full_weeks * 2, c - full_weeks * 2]
    
    # Try starting from each day of the week
    for start_day in range(7):
        current_food = remaining_food[:]
        days = 0
        for i in range(7):
            day = (start_day + i) % 7
            food_type = week_pattern[day]
            if current_food[food_type] > 0:
                current_food[food_type] -= 1
                days += 1
            else:
                break
        max_days = max(max_days, full_weeks * 7 + days)
    
    return max_days

import sys
input = sys.stdin.read
a, b, c = map(int, input().strip().split())
print(max_days_of_feeding(a, b, c))
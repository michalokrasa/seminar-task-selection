def calculate_midpoint(start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))

    start_total_minutes = start_hour * 60 + start_minute
    end_total_minutes = end_hour * 60 + end_minute

    midpoint_total_minutes = (start_total_minutes + end_total_minutes) // 2

    midpoint_hour = midpoint_total_minutes // 60
    midpoint_minute = midpoint_total_minutes % 60

    return f"{midpoint_hour:02}:{midpoint_minute:02}"

import sys

input = sys.stdin.read
data = input().strip().split()
start_time = data[0]
end_time = data[1]

print(calculate_midpoint(start_time, end_time))
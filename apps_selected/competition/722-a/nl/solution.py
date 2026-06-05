def correct_time(format_type, time_str):
    hours, minutes = map(int, time_str.split(':'))
    
    if format_type == 12:
        if hours < 1 or hours > 12:
            if hours == 0:
                hours = 1
            elif hours > 12:
                if hours % 10 == 0:
                    hours = 10
                else:
                    hours = hours % 10
                    if hours == 0:
                        hours = 1
        if minutes < 0 or minutes > 59:
            minutes = minutes % 60
    elif format_type == 24:
        if hours < 0 or hours > 23:
            hours = hours % 24
        if minutes < 0 or minutes > 59:
            minutes = minutes % 60
    
    return f"{hours:02}:{minutes:02}"

import sys
input = sys.stdin.read
data = input().split()
format_type = int(data[0])
time_str = data[1]
print(correct_time(format_type, time_str))
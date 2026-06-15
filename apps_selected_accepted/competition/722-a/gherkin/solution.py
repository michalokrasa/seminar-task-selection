def correct_time(format_type, time_str):
    hh, mm = map(int, time_str.split(':'))
    
    if format_type == 24:
        if hh >= 24:
            hh = hh % 10
        if mm >= 60:
            mm = mm % 10
    elif format_type == 12:
        if hh == 0 or hh > 12:
            hh = hh % 10
            if hh == 0:
                hh = 1
        if mm >= 60:
            mm = mm % 10

    return f"{hh:02}:{mm:02}"

import sys
input = sys.stdin.read
data = input().strip().split()
format_type = int(data[0])
time_str = data[1]
print(correct_time(format_type, time_str))
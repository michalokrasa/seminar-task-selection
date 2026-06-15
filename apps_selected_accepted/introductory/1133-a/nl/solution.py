def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    start_time = data[0]
    end_time = data[1]
    
    h1, m1 = map(int, start_time.split(':'))
    h2, m2 = map(int, end_time.split(':'))
    
    start_minutes = h1 * 60 + m1
    end_minutes = h2 * 60 + m2
    
    midpoint_minutes = (start_minutes + end_minutes) // 2
    
    midpoint_hour = midpoint_minutes // 60
    midpoint_minute = midpoint_minutes % 60
    
    print(f"{midpoint_hour:02}:{midpoint_minute:02}")

main()
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    current_time = data[0]
    minutes_to_add = int(data[1])
    
    hh, mm = map(int, current_time.split(':'))
    
    total_minutes = hh * 60 + mm + minutes_to_add
    
    new_hh = (total_minutes // 60) % 24
    new_mm = total_minutes % 60
    
    print(f"{new_hh:02}:{new_mm:02}")

main()
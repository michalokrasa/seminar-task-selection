def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    observed_colors = set(data[1:])
    
    color_to_gem = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }
    
    all_colors = set(color_to_gem.keys())
    absent_colors = all_colors - observed_colors
    
    absent_gems = [color_to_gem[color] for color in absent_colors]
    absent_gems.sort()
    
    print(len(absent_gems))
    for gem in absent_gems:
        print(gem)

main()
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    present_colors = set(data[1:n+1])
    
    gem_colors = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }
    
    missing_gems = []
    
    for color, gem in gem_colors.items():
        if color not in present_colors:
            missing_gems.append(gem)
    
    print(len(missing_gems))
    for gem in missing_gems:
        print(gem)

main()
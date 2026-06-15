def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    lengths = {}
    
    for line in data:
        choice = line[0]
        description = line[2:]
        lengths[choice] = len(description)
    
    great_choices = []
    
    for choice, length in lengths.items():
        is_great = True
        for other_choice, other_length in lengths.items():
            if choice != other_choice:
                if not (length >= 2 * other_length or length * 2 <= other_length):
                    is_great = False
                    break
        if is_great:
            great_choices.append(choice)
    
    if len(great_choices) == 1:
        print(great_choices[0])
    else:
        print('C')

main()
def count_excessive_shocks(actions):
    possible_letters = set('abcdefghijklmnopqrstuvwxyz')
    excessive_shocks = 0
    determined = False

    for action in actions:
        if action.startswith('.'):
            word = action[2:]
            possible_letters -= set(word)
        elif action.startswith('!'):
            word = action[2:]
            if determined:
                excessive_shocks += 1
            possible_letters &= set(word)
        elif action.startswith('?'):
            letter = action[2]
            if determined:
                excessive_shocks += 1
            possible_letters.discard(letter)

        if len(possible_letters) == 1:
            determined = True

    return excessive_shocks

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    n = int(data[0])
    actions = data[1:n+1]
    print(count_excessive_shocks(actions))
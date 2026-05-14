def simulate_voting_outcome(voter_sequence):
    from collections import deque

    n = len(voter_sequence)
    depublicans = deque()
    remocrats = deque()

    for i, voter in enumerate(voter_sequence):
        if voter == 'D':
            depublicans.append(i)
        else:
            remocrats.append(i)

    while depublicans and remocrats:
        d_index = depublicans.popleft()
        r_index = remocrats.popleft()

        if d_index < r_index:
            depublicans.append(d_index + n)
        else:
            remocrats.append(r_index + n)

    return 'D' if depublicans else 'R'

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip()
    print(simulate_voting_outcome(data))
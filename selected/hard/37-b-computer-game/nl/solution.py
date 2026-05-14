def computer_game(N, max_hp, reg, scrolls):
    from heapq import heappush, heappop
    import sys

    # Sort scrolls by power percentage
    scrolls.sort()

    # Priority queue for active spells (damage, index)
    active_spells = []
    total_damage = 0
    current_hp = max_hp
    time = 0
    used_scrolls = []

    # Function to check if we can use a scroll
    def can_use_scroll(scroll, current_hp):
        powi, _ = scroll
        return current_hp <= (powi * max_hp) // 100

    # Try to use scrolls optimally
    while current_hp > 0:
        # Check if we can use any scroll
        for i, scroll in enumerate(scrolls):
            if can_use_scroll(scroll, current_hp):
                powi, dmgi = scroll
                heappush(active_spells, (-dmgi, i))
                used_scrolls.append((time, i + 1))
                break

        # Apply damage from active spells
        current_hp -= total_damage

        # Check if boss is defeated
        if current_hp <= 0:
            print("YES")
            print(time, len(used_scrolls))
            for second, index in used_scrolls:
                print(second, index)
            return

        # Regenerate boss HP
        current_hp = min(max_hp, current_hp + reg)

        # Increment time
        time += 1

        # Update total damage from active spells
        while active_spells and active_spells[0][0] == -total_damage:
            heappop(active_spells)
        total_damage = -sum(d for d, _ in active_spells)

    print("NO")

# Read input
input_data = sys.stdin.read().strip().split()
N = int(input_data[0])
max_hp = int(input_data[1])
reg = int(input_data[2])
scrolls = []

for i in range(N):
    powi = int(input_data[3 + 2 * i])
    dmgi = int(input_data[4 + 2 * i])
    scrolls.append((powi, dmgi))

computer_game(N, max_hp, reg, scrolls)
def boss_battle_optimiser():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    max_hp = int(data[1])
    reg = int(data[2])
    
    scrolls = []
    index = 3
    for i in range(N):
        powi = int(data[index])
        dmgi = int(data[index + 1])
        scrolls.append((powi, dmgi, i + 1))
        index += 2
    
    # Sort scrolls by power percentage descending, then by damage descending
    scrolls.sort(key=lambda x: (-x[0], -x[1]))
    
    current_hp = max_hp
    active_damage = 0
    time = 0
    used_scrolls = []
    
    while current_hp > 0:
        # Apply damage
        current_hp -= active_damage
        
        # Check if boss is defeated
        if current_hp <= 0:
            print("YES")
            print(time, len(used_scrolls))
            for t, idx in used_scrolls:
                print(t, idx)
            return
        
        # Regenerate HP
        current_hp = min(current_hp + reg, max_hp)
        
        # Try to use a scroll
        for powi, dmgi, idx in scrolls:
            if current_hp <= (powi * max_hp) // 100:
                active_damage += dmgi
                used_scrolls.append((time, idx))
                scrolls.remove((powi, dmgi, idx))
                break
        
        # Increment time
        time += 1
        
        # If no scrolls left and damage is not enough to overcome regeneration
        if not scrolls and active_damage <= reg:
            print("NO")
            return
    
    # If we exit the loop without defeating the boss
    print("NO")

boss_battle_optimiser()
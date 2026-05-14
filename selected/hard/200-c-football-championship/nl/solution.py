from itertools import permutations

def parse_game_result(line):
    team1, team2, score = line.split()
    goals1, goals2 = map(int, score.split(':'))
    return team1, team2, goals1, goals2

def update_table(table, team1, team2, goals1, goals2):
    if team1 not in table:
        table[team1] = {'points': 0, 'goal_difference': 0, 'goals_scored': 0}
    if team2 not in table:
        table[team2] = {'points': 0, 'goal_difference': 0, 'goals_scored': 0}
    
    table[team1]['goals_scored'] += goals1
    table[team2]['goals_scored'] += goals2
    table[team1]['goal_difference'] += goals1 - goals2
    table[team2]['goal_difference'] += goals2 - goals1
    
    if goals1 > goals2:
        table[team1]['points'] += 3
    elif goals1 < goals2:
        table[team2]['points'] += 3
    else:
        table[team1]['points'] += 1
        table[team2]['points'] += 1

def can_berland_qualify(table, berland, opponent, x, y):
    table_copy = {team: stats.copy() for team, stats in table.items()}
    update_table(table_copy, berland, opponent, x, y)
    
    standings = sorted(table_copy.items(), key=lambda item: (
        -item[1]['points'], 
        -item[1]['goal_difference'], 
        -item[1]['goals_scored'], 
        item[0]
    ))
    
    for i, (team, _) in enumerate(standings):
        if team == berland:
            return i < 2
    return False

def find_minimal_win_score(berland, opponent, table):
    for margin in range(1, 100):  # Arbitrary large number for margin
        for y in range(100):  # Arbitrary large number for goals conceded
            x = y + margin
            if can_berland_qualify(table, berland, opponent, x, y):
                return f"{x}:{y}"
    return "IMPOSSIBLE"

def main():
    games = [input().strip() for _ in range(5)]
    table = {}
    teams = set()
    
    for game in games:
        team1, team2, goals1, goals2 = parse_game_result(game)
        update_table(table, team1, team2, goals1, goals2)
        teams.update([team1, team2])
    
    berland = "BERLAND"
    opponent = (teams - {berland}).pop()
    
    result = find_minimal_win_score(berland, opponent, table)
    print(result)

main()
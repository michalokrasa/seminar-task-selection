def parse_game_result(game_result):
    team1, team2, goals = game_result.split()
    goals1, goals2 = map(int, goals.split(':'))
    return team1, team2, goals1, goals2

def update_standings(standings, team, scored, conceded):
    if team not in standings:
        standings[team] = {'points': 0, 'goal_difference': 0, 'goals_scored': 0}
    standings[team]['goal_difference'] += scored - conceded
    standings[team]['goals_scored'] += scored
    if scored > conceded:
        standings[team]['points'] += 3
    elif scored == conceded:
        standings[team]['points'] += 1

def calculate_standings(games):
    standings = {}
    for game in games:
        team1, team2, goals1, goals2 = parse_game_result(game)
        update_standings(standings, team1, goals1, goals2)
        update_standings(standings, team2, goals2, goals1)
    return standings

def berland_minimum_win_score(games):
    standings = calculate_standings(games)
    berland_games = [game for game in games if 'BERLAND' in game]
    if len(berland_games) != 2:
        return "IMPOSSIBLE"
    
    # Find the opponent in the last game
    last_game = berland_games[1]
    team1, team2, goals1, goals2 = parse_game_result(last_game)
    opponent = team1 if team2 == 'BERLAND' else team2
    
    # Remove the last game from standings
    standings[team1]['goal_difference'] -= goals1 - goals2
    standings[team1]['goals_scored'] -= goals1
    standings[team2]['goal_difference'] -= goals2 - goals1
    standings[team2]['goals_scored'] -= goals2
    if goals1 > goals2:
        standings[team1]['points'] -= 3
    elif goals1 == goals2:
        standings[team1]['points'] -= 1
        standings[team2]['points'] -= 1
    else:
        standings[team2]['points'] -= 3

    # Try to find the minimum winning score for BERLAND
    min_diff = float('inf')
    best_score = "IMPOSSIBLE"
    
    for x in range(1, 101):
        for y in range(0, x):
            # Simulate the game with BERLAND winning x:y
            standings_copy = {team: standings[team].copy() for team in standings}
            standings_copy['BERLAND']['goal_difference'] += x - y
            standings_copy['BERLAND']['goals_scored'] += x
            standings_copy['BERLAND']['points'] += 3
            standings_copy[opponent]['goal_difference'] -= x - y
            standings_copy[opponent]['goals_scored'] += y
            
            # Sort teams based on the ranking criteria
            sorted_teams = sorted(standings_copy.items(), key=lambda item: (
                -item[1]['points'],
                -item[1]['goal_difference'],
                -item[1]['goals_scored'],
                item[0]
            ))
            
            # Check if BERLAND is in the top 2
            if sorted_teams[0][0] == 'BERLAND' or sorted_teams[1][0] == 'BERLAND':
                if x - y < min_diff or (x - y == min_diff and y < int(best_score.split(':')[1])):
                    min_diff = x - y
                    best_score = f"{x}:{y}"
    
    return best_score

# Read input
import sys
games = [input().strip() for _ in range(5)]
print(berland_minimum_win_score(games))
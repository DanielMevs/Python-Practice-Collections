def find_winner(player_scores):
    highest_avg = 0
    highest_avg_player = ''
    for player, scores in player_scores.items():
        avg = sum(scores) / len(scores)
        if avg > highest_avg:
            highest_avg = avg
            highest_avg_player = player
    return [highest_avg_player, highest_avg]
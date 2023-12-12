from statistics import mean

def find_winner(player_scores):
#     # Your code goes here
#     
    return list(max(list(zip(player_scores.keys(), list(mean(vals) for vals in player_scores.values()))), key=lambda item: item[1]))




scores = {'Alice': [3, 6], 'Bob': [2, 6], 'Charles': [1, 5]}
print(find_winner(scores))
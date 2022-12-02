# The mapping between moves and numbers
key = { 'A': 0, # Rock
        'B': 1, # Paper
        'C': 2, # Scissors
        'X': 0, # Rock
        'Y': 1, # Paper
        'Z': 2} # Scissors

scores = {'A': 1,
          'B': 2,
          'C': 3,
          'X': 1,
          'Y': 2,
          'Z': 3}

# Win-lose matrix
win_lose = [[-1,  1,  0], # Rock
            [ 1, -1,  2], # Paper
            [ 0,  2, -1]] # Scissors
            #Roc Pap Sci

# read given input into python
with open('input.txt') as input_text:
    game = input_text.read().split('\n')
    game = [pair.split(' ') for pair in game]
    print(game)
input_text.close()

# Part 1
# What would your total score be if everything goes exactly according to your strategy guide?
final_score = 0
for g in game :
    op = g[0]
    me = g[1]
    result = win_lose[key.get(op)][key.get(me)]
    score = scores.get(me)
    if result == key.get(me):
        score += 6
    elif result == -1:
        score += 3
    print(score)
    final_score += score

print(final_score)

# Part 2
# What would your total score be if everything goes exactly according to your strategy guide?
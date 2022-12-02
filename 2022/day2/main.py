# The mapping between moves and numbers
opponent = {0: 'A', # Rock
            1: 'B', # Paper
            2: 'C'} # Scissors
me = {0: 'X', # Rock
      1: 'Y', # Paper
      2: 'Z'} # Scissors

scores = {'A': 1,
          'B': 2,
          'C': 3,
          'X': 1,
          'Y': 2,
          'Z': 3}

# Win-lose matrix
win_lose = [[-1, 1, 0],
            [1, -1, 2],
            [0, 2, -1]]

# read given input into python
with open('input.txt') as input_text:
    game = input_text.read().split('\n')
    game = [pair.split(' ') for pair in game]
    print(game)
input_text.close()

# Part 1
# What would your total score be if everything goes exactly according to your strategy guide?

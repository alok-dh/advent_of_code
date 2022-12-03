# The mapping between moves and numbers
from enum import Enum


class Move(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Outcome(Enum):
    Lose = 0
    Win = 6
    Draw = 3


key = {'A': 0,  # Rock
       'B': 1,  # Paper
       'C': 2,  # Scissors
       'X': 0,  # Rock
       'Y': 1,  # Paper
       'Z': 2}  # Scissors

scores = {'A': 1,
          'B': 2,
          'C': 3,
          'X': 1,
          'Y': 2,
          'Z': 3}

outcomes = {'X': 0,
            'Y': 3,
            'Z': 6}

# Win-lose matrix
win_lose = [[-1, 1, 0],  # Rock [0,0] [0,1], [0,2]
            [1, -1, 2],  # Paper
            [0, 2, -1]]  # Scissors
#           Roc Pap Sci

# win lose array
win_lose_array = [0, 1, 2]

# read given input into python
with open('input.txt') as input_text:
    raw = input_text.readlines()
    game = [pair.strip().split(' ') for pair in raw]
    print(game)
input_text.close()

# Part 1
# What would your total score be if everything goes exactly according to your strategy guide?
final_score = 0
for g in game:
    op = g[0]
    me = g[1]
    result = win_lose[key[op]][key[me]]
    score = scores[me]
    if result == key[me]:
        score += Outcome.Win.value
    elif result == -1:
        score += Outcome.Draw.value
    print(score)
    final_score += score

print(final_score)

final_score = 0
for g in game:
    move = g[0]
    required_outcome = g[1]
    opponents_play = Move(scores[move])
    print(opponents_play)
    my_outcome = Outcome(outcomes[required_outcome])
    print(my_outcome)
    final_score += my_outcome.value
    match my_outcome:
        case Outcome.Draw:
            final_score += opponents_play.value
        case Outcome.Win:
            results = win_lose[key[move]]
            for i, j in enumerate(results):
                if i == j:
                    final_score += i+1
                    break
        case Outcome.Lose:
            results = win_lose_array[(key[move] - 1) % 3]
            print(key[move])
            print(results)
            final_score += results + 1
    print(final_score)





#def b_wins(a: Move, b: Move) -> Outcome:
#    if a == b:
#        return Outcome.Draw
#    return Outcome.Lose if Move(((a.value + 1) % 3) + 1) == b else Outcome.Win
#
#
#def play(game: list[(Move, Move)]) -> int:
#    score = 0
#    for a, b in game:
#        score += b_wins(a, b).value + b.value
#    return score
#
#
#def parse_input(data_file: str) -> list[(Move, Move)]:
#    with open(data_file) as f:
#        game_raw = [pair.strip().split() for pair in f.readlines()]
#        return [(Move(scores[a]), Move(scores[b])) for a, b in game_raw]
#
#
#def main():
#    game = parse_input('input.txt')
#    print(f"Part 1: {play(game)}")
#
#
#if __name__ == "__main__":
#    main()
#    raise SystemExit(0)

# Part 2
# What would your total score be if everything goes exactly according to your strategy guide?

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


values = {'A': 1,
          'B': 2,
          'C': 3,
          'X': 1,
          'Y': 2,
          'Z': 3}

outcomes = {'X': 0,
            'Y': 3,
            'Z': 6}


def parse_input(data_file: str) -> list[(Move, Move)]:
    with open(data_file) as input_text:
        moves = [pair.strip().split() for pair in input_text.readlines()]
        return [(Move(values[a]), Move(values[b]), Outcome(outcomes[b])) for a, b in moves]


def determine_winner(a: Move, b: Move) -> Outcome:
    if a == b:
        return Outcome.Draw
    else:
        return Outcome.Lose if Move(((a.value + 1) % 3) + 1) == b else Outcome.Win


# Part 1
# What would your total score be if everything goes exactly according to your strategy guide?
def part_one(moves: list[(Move, Move, Outcome)]) -> int:
    ans = 0
    for a, b, c in moves:
        ans += determine_winner(a, b).value + b.value
    return ans


def determine_play(a: Move, c: Outcome) -> Move:
    match c:
        case Outcome.Draw:
            return a
        case Outcome.Win:
            return Move(((a.value + 1) % 3) + 1)
        case Outcome.Lose:
            return Move(((a.value - 1) % 3) + 1)


# Part 2
# What would your total score be if everything goes exactly according to your strategy guide?
def part_two(moves: list[(Move, Move, Outcome)]) -> int:
    ans = 0
    for a, b, c in moves:
        print(f"play {determine_play(a, c).value + c.value}")
        ans += determine_play(a, c).value + c.value
    return ans


# final_score = 0
# for g in game:
#     move = g[0]
#     required_outcome = g[1]
#     opponents_play = Move(values[move])
#     print(opponents_play)
#     my_outcome = Outcome(outcomes[required_outcome])
#     print(my_outcome)
#     final_score += my_outcome.value
#     match my_outcome:
#         case Outcome.Draw:
#             final_score += opponents_play.value
#         case Outcome.Win:
#             results = win_lose[key[move]]
#             for i, j in enumerate(results):
#                 if i == j:
#                     final_score += i + 1
#                     break
#         case Outcome.Lose:
#             results = win_lose_array[(key[move] - 1) % 3]
#             print(key[move])
#             print(results)
#             final_score += results + 1
#     print(final_score)

def main():
    inputs = parse_input('input.txt')
    print(f"Part 1: {part_one(inputs)}")
    print(f"Part 2: {part_two(inputs)}")


if __name__ == "__main__":
    main()
    raise SystemExit(0)

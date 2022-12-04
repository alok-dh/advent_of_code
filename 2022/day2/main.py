# The mapping between moves and numbers
from enum import Enum


# Move Enum where hierarchy can be determined by:
#   (Move.value % 3) + 1 beats Move
#   (Move.vale + 1)  % 3) + 1 looses to Move
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


# Return triples of Move a, Move b, and Part 2's Outcome
def parse_input(data_file: str) -> list[(Move, Move, Outcome)]:
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
        case Outcome.Win:  # Return the move required to win
            return Move((a.value % 3) + 1)
        case Outcome.Lose:  # Return the move required to lose
            return Move(((a.value + 1) % 3) + 1)  #


# Part 2
# What would your total score be if everything goes exactly according to your strategy guide?
def part_two(moves: list[(Move, Move, Outcome)]) -> int:
    ans = 0
    for a, b, c in moves:
        ans += determine_play(a, c).value + c.value
    return ans


def main():
    inputs = parse_input('input.txt')
    print(f"Part 1: {part_one(inputs)}")
    print(f"Part 2: {part_two(inputs)}")


if __name__ == "__main__":
    main()
    raise SystemExit(0)

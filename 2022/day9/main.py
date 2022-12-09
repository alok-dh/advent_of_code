# read given input into python
with open('input.txt') as input_text:
    moves = [pair.strip().split(" ") for pair in input_text.readlines()]

# Part 1
# Simulate your complete hypothetical series of motions.
# How many positions does the tail of the rope visit at least once?
# tail = [[0, 0] for _ in range(2)] # use for part one
# Part 2
# Simulate your complete series of motions on a larger rope with ten knots.
# How many positions does the tail of the rope visit at least once?
tail = [[0, 0] for _ in range(10)]  # use for part two
move = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
seen = set()
for direction, distance, in moves:
    for step in range(int(distance)):
        tail[0][0] += move[direction][0]
        tail[0][1] += move[direction][1]
        for i in range(1, len(tail)):
            x_cord, y_cord = tail[i-1][0] - tail[i][0], tail[i-1][1] - tail[i][1]
            if max(abs(x_cord), abs(y_cord)) > 1:
                tail[i][0] += (1 if x_cord > 0 else 0 if x_cord == 0 else -1)
                tail[i][1] += (1 if y_cord > 0 else 0 if y_cord == 0 else -1)
        seen.add(tuple(tail[-1]))
print(len(seen))





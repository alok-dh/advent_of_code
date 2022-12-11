# read given input into python
with open('input.txt') as input_text:
    instructions = [pair.strip().split(" ") for pair in input_text.readlines()]

# Part 1
# Find the signal strength during the 20th,
# 60th, 100th, 140th, 180th, and 220th cycles.
# What is the sum of these six signal strengths?
x = 1
cycle = 0
values = {}
checkpoints = (20, 60, 100, 140, 180, 220)
signal_strength = 0
for operation in instructions:
    match operation:
        case [_, value]:
            cycle += 1
            values[cycle] = x
            cycle += 1
            values[cycle] = x
            x += int(value)
        case _:
            cycle += 1
            values[cycle] = x

for cycle in checkpoints:
    signal_strength += values[cycle] * cycle
print(signal_strength)

# Part 2
# Render the image given by your program.
# What eight capital letters appear on your CRT?
crt = [['.' for x in range(40)] for y in range(6)]
for cycle in values:
    x = values[cycle]
    y = cycle - 1
    row = cycle // 40
    col = y - (row * 40)
    if y % 40 in (x - 1, x, x + 1):
        crt[row][col] = '#'
for pixel in crt:
    print(''.join(pixel))


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
for operation in instructions:
    match operation:
        case [_, value]:
            cycle += 1
            values[cycle] = (x, x * cycle)
            cycle += 1
            values[cycle] = (x, x * cycle)
            x += int(value)
        case _:
            cycle += 1
            values[cycle] = (x, x * cycle)

checkpoints = (20, 60, 100, 140, 180, 220)
signal_strength = 0
for checkpoint in checkpoints:
    signal_strength += values[checkpoint][1]
print(signal_strength)
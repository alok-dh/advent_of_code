# read given input into python
with open('test.txt') as input_text:
    crates_diagram, moves = [text.strip().split("\n") for text in input_text.read().split("\n\n")]

# Crates Diagram
#
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# Moves
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# Part 1
# After the rearrangement procedure completes,
# what crate ends up on top of each stack?
crates = [[] for _ in crates_diagram[0][1::4]]
for row in crates_diagram[-2::-1]:  # flip and remove index number
    # very cool inspired by reddit see:
    # [Z] [M] [P]
    # [N] [C]
    #     [D]
    for i, crate in enumerate(row[1::4]):
        if crate != " ":
            crates[i].append(crate)

for move in moves:
    _, x_many, _, from_y, _, to_z = move.split()
    for i in range(int(x_many)):
        # crates[int(to_z) - 1].append(crates[int(from_y) - 1].pop())  # part 1
        # Part 2
        # Before the rearrangement process finishes,
        # update your simulation so that the Elves know where
        # they should stand to be ready to unload the final supplies.
        # After the rearrangement procedure completes,
        # what crate ends up on top of each stack?
        crates[int(to_z) - 1].insert(len(crates[int(to_z) - 1]), crates[int(from_y) - 1].pop())  # part 2
print("".join(c[-1] for c in crates))

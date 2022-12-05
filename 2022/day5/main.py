# read given input into python
with open('input.txt') as input_text:
    crates_diagram, moves = [text.strip().split("\n") for text in input_text.read().split("\n\n")]
    # moves = moves_text.splitlines()
    print(crates_diagram)

# Part 1
# After the rearrangement procedure completes,
# what crate ends up on top of each stack?
crates = [[] for _ in crates_diagram[0][1::4]]
for row in crates_diagram[-2::-1]:  # flip and remove index number
    print(row)
    for i, crate in enumerate(row[1::4]):
        if crate != " ":
            crates[i].append(crate)
print(crates)

instrctions = []
for move in moves:
    _, x_many, _, from_y, _, to_z = move.split()
    instrctions.append([int(x_many), int(from_y), int(to_z)])
print(instrctions)





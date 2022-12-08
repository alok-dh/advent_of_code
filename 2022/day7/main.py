from collections import defaultdict

# read given input into python
with open('input.txt') as input_text:
    commands = [text.strip() for text in input_text.readlines()]

path = []
ans = defaultdict(int)  # cleaned solution using defaultdic inspired by u/joshbduncan from r/adventofcode
for command in commands:
    c = command.split()
    match c:  # I use a switch because aesthetics even if it forces me to use multiple pass cases...
        case['$', 'ls']:
            pass
        case['dir', name]:
            pass
        case ['$', 'cd', '/']:
            path.append('/')
        case ['$', 'cd', '..']:
            path.pop()
        case ['$', 'cd', directory]:
            if path[-1] == '/':
                path.append(f"{directory}")
            else:
                path.append(f"{path[-1]}/{directory}")
        case [size, _]:
            for dirr in path:
                ans[dirr] += int(size)
print(ans)
# Part 1
# Find all directories with a total size of at most 100000.
# What is the sum of the total sizes of those directories?
print(f"Part 1: {sum(s for s in ans.values() if s <= 100000)}")
# Part 2
# Find the smallest directory that, if deleted,
# would free up enough space (30000000) on the filesystem to run the update.
# What is the total size of that directory?
print(f"Part 2: {min(s for s in ans.values() if s >= 30000000 - (70000000 - ans['/']))}")





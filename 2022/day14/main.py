with open('input.txt') as input_text:
    lines = [line.split(' -> ') for line in input_text.read().strip().splitlines()]
    print(lines)
    coords = [[tuple(map(int, l.split(","))) for l in line] for line in lines]
    print(coords)

cave = set()
max_y = max([c[1] for line in coords for c in line])
xs = [c[0] for line in coords for c in line]
max_x, min_x = max(xs), min(xs)
for cord in coords:
    x, y = cord.pop(0)
    cave.add((x, y))
    for to_x, to_y in cord:
        dx, dy = to_x - x, to_y - y
        if dx != 0: dx = dx // abs(dx)
        if dy != 0: dy = dy // abs(dy)
        while x != to_x or y != to_y:
            x += dx
            y += dy
            cave.add((x, y))

source = (500, 0)
current = source
max_y = max_y + 2
for i in range(min_x - min_x//2, max_x + max_x//2): cave.add((i, max_y))
print(sorted(cave))
num_rocks = len(cave)
while current[1] < max_y:
    (c, r) = current
    if (c, r + 1) not in cave: current = (c, r + 1)
    elif (c - 1, r + 1) not in cave: current = (c - 1, r + 1)
    elif (c + 1, r + 1) not in cave: current = (c + 1, r + 1)
    else:
        if source in cave: break
        cave.add(current)
        current = source
print(f"{len(cave) - num_rocks}")
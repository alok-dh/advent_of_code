# read given input into python
import math
import string
from collections import defaultdict, deque

with open('test.txt') as input_text:
    # instructions = [pair.strip().split(" ") for pair in input_text.readlines()]
    heightmap = [line.strip() for line in input_text.readlines()]
    # heightmap = input_text.read()
    print(heightmap)


class Node:

    def __init__(self, xy: tuple, value: chr):
        self.xy = xy
        self.value = value
        self.children = []
        self.visited = False
        self.dist = math.inf


def evaluate(v: chr) -> int:
    elevation = string.ascii_lowercase
    if v == 'S':
        return elevation.index('a')
    elif v == 'E':
        return elevation.index('z')
    else:
        return elevation.index(v)


width, height = len(heightmap[0]), len(heightmap)
mountain, start, end = [], None, None
for row in heightmap:
    x = heightmap.index(row)
    for val in row:
        y = row.index(val)
        node = Node((x, y), val)
        mountain.append(node)
        if val == 'S':
            start = node
        elif val == 'E':
            end = node
        for r, c in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if r == -1 or c == -1:
                continue
            elif r >= height or c >= width:
                continue
            elif evaluate(node.value) > evaluate(heightmap[r][c]) + 1:
                continue
            else:
                node.children.append(Node((r, c), evaluate(heightmap[r][c])))

for m in mountain:
    print(m.__dict__)

# start = [k for k in mountain if mountain[k] == 'S']
# end = [k for k in mountain if mountain[k] == 'E']
seen = [start]
shortest_path = defaultdict(int)
shortest = math.inf
while seen:
    current = seen.pop()
    current.visited = True
    # next_step = steps + 1
    x, y = current.xy
    if current.dist < shortest: shortest = current.dist
    if (x, y) == end.xy:
        shortest = min(shortest, current.dist)
        break
    for n in current.children:
        if not n.visited:
            if n.dist + 1 < current.dist:
                current.dist = n.dist

print(shortest)

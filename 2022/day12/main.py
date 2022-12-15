# read given input into python
import string
from collections import defaultdict, deque

with open('test.txt') as input_text:
    # instructions = [pair.strip().split(" ") for pair in input_text.readlines()]
    heightmap = [line.strip() for line in input_text.readlines()]
    # heightmap = input_text.read()
    print(heightmap)


class Node:

    def __init__(self, xy: tuple, value: chr, children: list):
        self.xy = xy
        self.value = value
        self.children = children


elevation = string.ascii_lowercase
mountain = defaultdict(str)
for row in heightmap:
    x = heightmap.index(row)
    for val in row:
        y = row.index(val)
        mountain[(x, y)] = val
print(mountain)

start = [k for k in mountain if mountain[k] == 'S']
end = [k for k in mountain if mountain[k] == 'E']
seen = deque(((mountain[0,0], 0),))

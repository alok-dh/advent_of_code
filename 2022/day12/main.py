# read given input into python
import string

with open('test.txt') as input_text:
    # instructions = [pair.strip().split(" ") for pair in input_text.readlines()]
    heightmap = [line.strip() for line in input_text.readlines()]
    # heightmap = input_text.read()

elevation = string.ascii_lowercase
print(heightmap)
print(elevation)

class Node():

    def __init__(self, value: chr, children: list):
        self.value = value
        self.children = children
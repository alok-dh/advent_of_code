# read given input into python
import re

with open('test.txt') as input_text:
    text = [[m.strip() for m in line.split('\n')] for line in input_text.read().split('\n\n')]
    print(text)


class Monkey:

    def __init__(self, number: int, items: list, operation, test):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test

    def update_items(self, item):
        self.items.append(item)

    # def do_operation(self, new, old) -> int:
    #     return self.operation(new, old)

# construct a monke
monkeys = {}
for monke in text:
    num = [int(i) for i in re.findall('\d', monke[0])]
    items = [int(i) for i in re.findall('\d\d', monke[1])]
    print(items)



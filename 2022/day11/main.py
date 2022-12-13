import math
import re
from copy import deepcopy

# read given input into python
with open('input.txt') as input_text:
    text = [[m.strip() for m in line.split('\n')] for line in input_text.read().split('\n\n')]
    print(text)


class Operation:

    def __init__(self, operation: str, x) -> int:
        self.x = x
        self.operation = operation

    def do_operation(self, old):
        new_x = self.x
        if self.x == 'old':
            new_x = old
        match self.operation:
            case '+':
                return old + int(new_x)
            case '-':
                return old - int(new_x)
            case '*':
                return old * int(new_x)
            case '/':
                return old // int(new_x)


class Monkey:

    def __init__(self, number: int, items: list, operation: Operation, test: int, t: int, f: int):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.t = t
        self.f = f
        self.inspected = 0

    def update_items(self, item):
        self.items.append(item)


# construct a monke
monkeys: list[Monkey] = [Monkey for i in range(len(text))]
for monke in text:
    number, items, operation, test, t, f = None, None, None, None, None, None
    for m in monke:
        match m.strip(':').split():
            case 'Monkey', num:
                number = int(num)
            case 'Operation:', _, '=', _, op, x:
                operation = Operation(op, x)
            case 'Test:', _, _, x:
                test = int(x)
            case 'If', 'true:', _, _, _, i:
                t = int(i)
            case 'If', 'false:', _, _, _, i:
                f = int(i)
            case other:
                items = [int(i) for i in re.findall('\d\d', m)]
    monkeys[number] = Monkey(number, items, operation, test, t, f)

monke_part_two = deepcopy(monkeys)
# Part 1
# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds.
# What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
for _ in range(20):
    for m in monkeys:
        while len(m.items) > 0:
            worry = m.items.pop(0)
            m.inspected += 1
            worry = m.operation.do_operation(worry)
            worry = worry // 3
            if (worry % m.test) == 0:
                monkeys[m.t].update_items(worry)
            else:
                monkeys[m.f].update_items(worry)

active_monkeys = sorted([m.inspected for m in monkeys])
print(active_monkeys)
print(active_monkeys[-2] * active_monkeys[-1])

# Part 2
# Worry levels are no longer divided by three after each item is inspected;
# you'll need to find another way to keep your worry levels manageable.
# Starting again from the initial state in your puzzle input,
# what is the level of monkey business after 10000 rounds?
divisors = [d.test for d in monke_part_two]
lcm = math.lcm(*divisors)
bignumber = 0
for _ in range(10000):
    for m in monke_part_two:
        while len(m.items) > 0:
            bignumber = m.items.pop(0)
            m.inspected += 1
            bignumber = m.operation.do_operation(bignumber)
            bignumber %= lcm
            if (bignumber % m.test) == 0:
                monke_part_two[m.t].update_items(bignumber)
            else:
                monke_part_two[m.f].update_items(bignumber)

active_monkeys = sorted([m.inspected for m in monke_part_two])
print(active_monkeys)
print(active_monkeys[-2] * active_monkeys[-1])


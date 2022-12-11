import operator
import re
from collections import defaultdict

# read given input into python
with open('test.txt') as input_text:
    text = [[m.strip() for m in line.split('\n')] for line in input_text.read().split('\n\n')]
    print(text)


class Operation:

    def __init__(self, operation: str, x) -> int:
        self.x = x
        self.operation = operation

    def do_operation(self, old):
        if self.operation == x:
            self.x = old
        match self.operation:
            case '+':
                return operator.add(old, int(self.x))
            case '-':
                return operator.sub(old, int(self.x))
            case '*':
                return operator.mul(old, int(self.x))
            case '/':
                return operator.truediv(old, int(self.x))


class Monkey:

    def __init__(self, number: int, items: list, operation: Operation, test: int, t: int, f: int):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.f = f
        self.t = t

    def __str__(self):
        return f"Monkey: {self.number}, Items: {self.items}"

    def update_items(self, item):
        self.items.append(item)


# construct a monke
monkeys = defaultdict()
for monke in text:
    for m in monke:
        number, items, operation, test, t, f = None, None, None, None, None, None
        print(m.strip(':').split())
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
for m in monkeys:
    print(monkeys[m])

import operator
import re
from collections import defaultdict

# read given input into python
with open('test.txt') as input_text:
    text = [[m.strip() for m in line.split('\n')] for line in input_text.read().split('\n\n')]
    print(text)

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

class Operation:

    def __init__(self, operation: str, x: int) -> int:
        self.x = x
        self.operation = operation

    def do_operation(self, old):
        match self.operation:
            case '+':
                return operator.add(old, self.x)
            case '-':
                return operator.sub(old, self.x)
            case '*':
                return operator.mul(old, self.x)
            case '/':
                return operator.truediv(old, self.x)


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
        print(m.strip(':').split())
        match m.strip(':').split():
            case 'Monkey', num:
                number = int(num)
            case 'Operation:', _, '=', _, op, x:
                op = Operation(op, int(x))
            case 'Test:', _, _, x:
                test = int(x)
            case 'If', 'true:', _, _, _, i:
                t = int(i)
            case 'If', 'false:', _, _, _, i:
                f = int(i)
            case other:
                print(m)
                items = [int(i) for i in re.findall('\d\d', m)]
                print(items)

        print(m.strip(':').split())




#     num = [int(i) for i in re.findall('\d', monke[0])]
#     items = [int(i) for i in re.findall('\d\d', monke[1])]
#
#     monkeys[num[0]] = Monkey(num[0], items)
# for m in monkeys:
#     print(monkeys[m])

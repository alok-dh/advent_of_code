import re

ls = '$ ls'

def is_file(text) -> bool:
    return bool(re.search(r'\d', text))

# read given input into python
with open('test.txt') as input_text:
    commands = [text.strip() for text in input_text.readlines()]
    print(commands)

ans = 0
for c in commands:
    print(is_file(c))

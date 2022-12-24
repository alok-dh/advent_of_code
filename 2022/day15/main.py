with open('test.txt') as input_text:
    lines = [[l.split() for l in line.strip().split(': ')] for line in input_text.readlines()]
    print(lines)

for l in lines[0]:
    print(l[3].isnumeric())
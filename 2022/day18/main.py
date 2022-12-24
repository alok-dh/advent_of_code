with open("test.txt") as f:
    text = [[int(l) for l in line.strip().split(',')] for line in f.readlines()]
    print(text)

area = 0
for x, y, z in text:
    for p, q, s, in ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)):
        if [p, q, s] not in text: area += 1
print(area)


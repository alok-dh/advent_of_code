with open("input.txt") as f:
    text = [[int(l) for l in line.strip().split(',')] for line in f.readlines()]
    print(text)

# Part 1
# What is the surface area of your scanned lava droplet?
area = 0
for x, y, z in text:
    for p, q, s, in ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)):
        if [p, q, s] not in text: area += 1
print(area)

# Part 2
# What is the exterior surface area of your scanned lava droplet?
area = 0
for x, y, z in text:
    for p, q, s, in ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)):
        if [p, q, s] not in text:
            area += 1
            count = 0
            for x2, y2, z2, in ((p + 1, q, s), (p - 1, q, s), (p, q + 1, s), (p, q - 1, s), (p, q, s + 1), (p, q, s - 1)):
                if [x2, y2, z2] in text:
                    count += 1
            if count == 6: area -= 1
print(area)
with open("input.txt") as f:
    cubes = [[int(l) for l in line.strip().split(',')] for line in f.readlines()]
    print(cubes)

# Part 1
# What is the surface area of your scanned lava droplet?
area = 0
for x, y, z in cubes:
    for p, q, s, in ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)):
        if [p, q, s] not in cubes: area += 1
print(area)

# Part 2
# What is the exterior surface area of your scanned lava droplet?
exterior_area = 0
seen = set()
queue = [(0, 0, 0)]
while queue:
    x, y, z = queue.pop()
    seen.add((x, y, z))
    for p, q, s, in ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)):
        if -1 <= p <= 22 and -1 <= q <= 22 and -1 <= z <= 22 \
                and (p, q, s) not in seen and (p, q, s) not in queue:
            if [p, q, s] in cubes:
                exterior_area += 1
            else:
                queue.append((p, q, s))
print(exterior_area)

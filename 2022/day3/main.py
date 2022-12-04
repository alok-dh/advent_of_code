
# read given input into python
with open('input.txt') as input_text:
    raw = input_text.readlines()
    rucksack = [[item for item in items if item != '\n'] for items in raw]
#   make my containers tuples of sets to remove duplicate items in common
    containers = [[set(contents[len(contents) // 2:]), set(contents[:len(contents) // 2])] for contents in rucksack]
    print(containers)

# Goes from 0-52 used for scoring priority via invoking the .index function
priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1
# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?
sum_of_priority = 0
for container in containers:
    common_item = container[0].intersection(container[1])
    sum_of_priority += priority.index(common_item.pop())

print(sum_of_priority)

# Part 2
# Find the item type that corresponds to the badges of each three-Elf group.
# What is the sum of the priorities of those item types?
# I don't want the split sets from part one
containers_part_two = [set(contents) for contents in rucksack]
i = 0
sum_of_badges = 0
while i < len(containers_part_two):
    # taking advantage of intersect to peak into all 3 sets in one go
    badge = containers_part_two[i].intersection(containers_part_two[i+1], containers_part_two[i+2])
    sum_of_badges += priority.index(badge.pop())
    i += 3
print(sum_of_badges)

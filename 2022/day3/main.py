
# read given input into python
with open('input.txt') as input_text:
    raw = input_text.readlines()
    rucksack = [[item for item in items if item != '\n'] for items in raw]
    containers = [[set(contents[len(contents) // 2:]), set(contents[:len(contents) // 2])] for contents in rucksack]
    print(containers)

priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1
# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?
sum_of_priority = 0
for container in containers:
    common_item = container[0].intersection(container[1])
    sum_of_priority += priority.index(common_item.pop())

print(sum_of_priority)




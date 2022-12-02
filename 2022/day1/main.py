# I use the given input to create an inventory of
# how many calories each elf is carrying.
elves = []
inventory = []
ans = 0
elf = 0

# read given input into python
with open('input.txt') as input_text:
    raw = input_text.readlines()
    for i in raw:
        # transform single elf inventory to int
        if i != "\n":
            inventory.append(int(i.strip()))
        # add elf to our list of inventory lists
        else:
            elves.append(inventory)
            inventory = []
input_text.close()

# Part 1
# Find the Elf carrying the most Calories.
# How many total Calories is that Elf carrying?
# Sum all elf inventories
elves = [sum(i) for i in elves] 
elves.sort(reverse=True)
ans = elves[0]
print(f"The top elf is carrying {ans} calories")

# Part 2
# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?
ans = sum(elves[0:3])
print(f"The top 3 elves are carrying {ans} calories")


# read given input into python
with open('test.txt') as input_text:
    raw = input_text.readlines()
    rucksack = [[item for item in items if item != '\n'] for items in raw]
    print(rucksack)
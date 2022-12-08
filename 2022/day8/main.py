# read given input into python
with open('test.txt') as input_text:
    trees = [text.strip() for text in input_text.readlines()]
    print(trees)
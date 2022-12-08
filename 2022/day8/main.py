# read given input into python
with open('test.txt') as input_text:
    trees = [[tree for tree in text.strip()] for text in input_text.readlines()]
    print(trees)

# Part 1
# Consider your map; how many trees are visible from outside the grid?
rows = len(trees[0])
cols = len(trees)
visible = rows*2 + (cols-2)*2
print(visible)
for i in range(1, cols):
    for j in range(1, rows):
        tree = trees[i][j]
        if tree > trees[i-1][j]:
            print(tree)
            visible += 1
            break
        elif tree > trees[i+1][j]:
            print(tree)
            visible += 1
            break
        elif tree > trees[i][j-1]:
            print(tree)
            visible += 1
            break
        elif tree > trees[i][j+1]:
            print(tree)
            visible += 1
            break
print(visible)

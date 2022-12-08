# read given input into python
with open('test.txt') as input_text:
    trees = [[int(t) for t in text.strip()] for text in input_text.readlines()]
    print(trees)


# Part 1
# Consider your map; how many trees are visible from outside the grid?
cols, rows = len(trees[0]), len(trees)
edges = 2 * (rows - 2 + cols)
visible = set()
print(edges)
for x in range(1, rows - 1):
    for y in range(1, cols - 1):
        tree = trees[x][y]
        flag = True
        # check up
        for i in range(0, x):
            # print(f"i:{i} when x {x}")
            if tree <= trees[i][y]:
                flag = False
                break
        if flag:
            print(f"up: [{x}][{y}] = {tree}")
            visible.add((x,y))
        # check down
        flag = True
        for i in range(x, rows):
            if tree <= trees[i][y]:
                flag = False
                break
        if flag:
            print(f"down: [{x}][{y}] = {tree}")
            visible.add((x,y))
        # check left
        flag = True
        for i in range(0, y):
            if tree <= trees[x][i]:
                flag = False
                break
        if flag:
            print(f"left: [{x}][{y}] = {tree}")
            visible.add((x,y))
        # check right
        flag = True
        for i in range(y+1, cols):
            # print(f"i:{i} when y{y}")
            if tree <= trees[x][i]:
                flag = False
                break
        if flag:
            print(f"right: [{x}][{y}] = {tree}")
            visible.add((x,y))

print(visible)
print(len(visible)+edges)

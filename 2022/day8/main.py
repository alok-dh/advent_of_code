# read given input into python
with open('input.txt') as input_text:
    trees = [[int(t) for t in text.strip()] for text in input_text.readlines()]

# Part 1
# Consider your map; how many trees are visible from outside the grid?
cols, rows = len(trees[0]), len(trees)
edges = 2 * (rows - 2 + cols)
visible = set()
for x in range(1, rows - 1):
    for y in range(1, cols - 1):
        tree = trees[x][y]
        # check up
        flag = True
        for i in range(0, x):
            if tree <= trees[i][y]:
                flag = False
                break
        if flag:
            visible.add((x, y))
        # check down
        flag = True
        for i in range(x + 1, rows):
            if tree <= trees[i][y]:
                flag = False
                break
        if flag:
            visible.add((x, y))
        # check left
        flag = True
        for i in range(0, y):
            if tree <= trees[x][i]:
                flag = False
                break
        if flag:
            visible.add((x, y))
        # check right
        flag = True
        for i in range(y + 1, cols):
            if tree <= trees[x][i]:
                flag = False
                break
        if flag:
            visible.add((x, y))

print(len(visible) + edges)

scenic_scores = dict()
for i in range(rows):
    for j in range(cols):
        up, down, left, right = 0, 0, 0, 0
        for offset in reversed(range(0, j)):
            up += 1
            if trees[i][j] <= trees[i][offset]:
                break
        for offset in range(j + 1, rows):
            down += 1
            if trees[i][j] <= trees[i][offset]:
                break
        for offset in reversed(range(0, i)):
            right += 1
            if trees[i][j] <= trees[offset][j]:
                break
        for offset in range(i + 1, cols):
            left += 1
            if trees[i][j] <= trees[offset][j]:
                break
        scenic_scores[(i, j)] = up * down * right * left

print(max(scenic_scores.values()))


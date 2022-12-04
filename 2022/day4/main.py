# read given input into python
with open('input.txt') as input_text:
    pairs = [[section.strip() for section in sections.split(',')] for sections in input_text.readlines()]

# Part 1
# In how many assignment pairs does one range fully contain the other?
ans = 0
for pair in pairs:
    a = pair[0].split('-')
    b = pair[1].split('-')
    assignment_one = set([int(i) for i in range(int(a[0]), int(a[1]) + 1)])
    assignment_two = set([int(i) for i in range(int(b[0]), int(b[1]) + 1)])
    if assignment_one.issubset(assignment_two):
        ans += 1
    elif assignment_two.issubset(assignment_one):
        ans += 1
print(ans)

# Part 2
# In how many assignment pairs do the ranges overlap?
ans = 0
for pair in pairs:
    a = pair[0].split('-')
    b = pair[1].split('-')
    assignment_one = set([int(i) for i in range(int(a[0]), int(a[1]) + 1)])
    assignment_two = set([int(i) for i in range(int(b[0]), int(b[1]) + 1)])
    result = set(x in assignment_one for x in assignment_two)
    for b in result:
        if b:
            ans += 1
print(ans)

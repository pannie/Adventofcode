file = open('text.txt').read().splitlines()
data = []

for line in file:
    data.append(line)

x = 0
y = 0
tree_count = 0

for line in data:

    if data[y][x % len(data[0])] == '#':
        tree_count += 1

    y += 1
    x += 3

print('tree count: ' + str(tree_count))

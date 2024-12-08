from collections import Counter

input = list()

with open("input/day_08.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

antenna_and_index = [[char, r, c]
                     for r, row in enumerate(input)
                     for c, char in enumerate(row)
                     if not char == '.']

antinote_grid = [['.' for _ in row]
                 for row in input]

for ant1, y1, x1 in antenna_and_index:
    for ant2, y2, x2 in antenna_and_index:
        if (ant1, y1, x1) == (ant2, y2, x2):
            continue
        if not ant1 == ant2:
            continue
        dy, dx = (y1 - y2, x1 - x2)
        if 0 <= y1 + dy < len(input) and 0 <= x1 + dx < len(input):
            antinote_grid[y1 + dy][x1 + dx] = '#'

res = dict(sum(map(Counter, antinote_grid), Counter()))

print(res['#'])
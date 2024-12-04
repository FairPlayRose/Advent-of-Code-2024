input = list()

with open("input/day_04.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

# find starting matches for X
def find_base_match(char, matrix):

    base_matches = [(row_index, column_index)
                    for row_index, row in enumerate(matrix)
                    for column_index, column in enumerate(row)
                    if char == column]

    return base_matches

def find_next_matches(word, steps: int, prev_matches: list[tuple[int,int]], matrix):

    n = len(matrix)
    m = len(matrix[0])

    offsets = [(i,j)
               for i in range(-1, 2)
               for j in range(-1, 2)
               if not (i,j) == (0,0)]

    next_matches = []

    for (prev_x, prev_y) in prev_matches:
        for offset_x, offset_y in offsets:
            is_matching = True
            for step in range(1,steps+1):
                i = prev_x + step * offset_x
                j = prev_y + step * offset_y
                if not (n > i >= 0 and m > j >= 0):
                    is_matching = False
                    break
                if not word[step] == matrix[i][j]:
                    is_matching = False
                    break
            if is_matching:
                next_matches.append((prev_x,prev_y))
                 
    return next_matches

x_match = find_base_match('X', input)
xmas_match = find_next_matches('XMAS', 3, x_match, input)

print(len(xmas_match))
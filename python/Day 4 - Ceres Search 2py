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

def find_next_matches(prev_matches: list[tuple[int,int]], matrix):

    n = len(matrix)
    m = len(matrix[0])

    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    xcrossmatch = list()

    for prev_x, prev_y in prev_matches:
        is_matching = True
        xcross_index = [(prev_x + offset_x, prev_y + offset_y) for offset_x, offset_y in offsets]
        
        for x_index, y_index in xcross_index:
            if not (n > x_index >= 0 and m > y_index >= 0): is_matching = False

        xcross = list()
        if is_matching: xcross = [matrix[i][j] for i,j in xcross_index]

        match xcross:
            case ['M', 'M', 'S', 'S'] | ['M', 'S', 'M', 'S'] | ['S', 'S', 'M', 'M'] | ['S', 'M', 'S', 'M']:
                pass
            case _:
                is_matching = False
        
        if is_matching:
            xcrossmatch.append((prev_x, prev_y))

    return xcrossmatch

a_match = find_base_match('A', input)

cross_match = find_next_matches(a_match, input)
print(len(cross_match))


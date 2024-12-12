input: list[str] = list()

with open("input/day_12.txt", "r") as file:
    for line in file:
        input.append([x for x in line.rstrip()])


def plantAreas(plant: str, pos: tuple[int,int], field: list[str]) -> tuple[int,int, set[tuple[int,int]]]:
    pos_y, pos_x = pos

    if not pos_y in range(0, len(field)) or not pos_x in range(0, len(field)):
        return (0,1,{}) #area, border
    
    if '#' == field[pos_y][pos_x]:
        return (0,0,{})
        
    if plant != field[pos_y][pos_x]:
        return (0,1,{}) #area, border
        

    new_pos = [(pos_y+dy,pos_x+dx) for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]]

    field[pos_y][pos_x] = '#'

    area, border = (1,0)
    pos_set = {pos}

    for new in new_pos:
        darea, dborder, dpos_set = plantAreas(plant, new, field)
        area += darea
        border += dborder
        pos_set = pos_set.union(dpos_set)
        

    return (area, border, pos_set)

check_sum = 0

for i in range(len(input)):
    for j in range(len(input)):
        if input[i][j] != '.':
            area, border, pos_set = plantAreas(input[i][j], (i,j), input)
            check_sum += area*border
            for pos_y, pos_x in pos_set:
                input[pos_y][pos_x] = '.'

print(check_sum)
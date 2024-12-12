from itertools import groupby

input: list[str] = list()

with open("input/day_12_test.txt", "r") as file:
    for line in file:
        input.append([x for x in line.rstrip()])


def plantAreas(plant: str, pos: tuple[int,int], field: list[str]) -> tuple[int,set[tuple[int,int]],set[tuple[int,int]]]:
    pos_y, pos_x = pos

    if not pos_y in range(0, len(field)) or not pos_x in range(0, len(field)):
        return (0,{},{pos}) #area, pos_set, border_set
    
    if '#' == field[pos_y][pos_x]:
        return (0,{},{}) #area, pos_set, border_set
        
    if plant != field[pos_y][pos_x]:
        return (0,{},{pos}) #area, pos_set, border_set
        

    new_pos = [(pos_y+dy,pos_x+dx) for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]]

    field[pos_y][pos_x] = '#'

    area = 1
    pos_set = {pos}
    border_set = set()

    for new in new_pos:
        darea, dpos_set, dborder_set = plantAreas(plant, new, field)
        area += darea
        pos_set = pos_set.union(dpos_set)
        border_set = border_set.union(dborder_set)
        #print(dborder_set, border_set)

    return (area, pos_set, border_set)

def detect_range(pos: list[tuple[int,int]]):
    pos_ys = [y for _,y in pos]
    for i, j in groupby(enumerate(pos_ys), lambda x: x[1] - x[0]):
        j = list(j)
        yield j[0][1], j[-1][1]

area, pos_set, border_set = plantAreas('R', (0,0), input)
border_list = list(border_set)
border_list.sort()
print(border_list)


#check_sum = 0
#
#for i in range(len(input)):
#    for j in range(len(input)):
#        if input[i][j] != '.':
#            area, border, pos_set, border_set = plantAreas(input[i][j], (i,j), input)
#            check_sum += area*border
#            for pos_y, pos_x in pos_set:
#                input[pos_y][pos_x] = '.'
#
#print(check_sum)
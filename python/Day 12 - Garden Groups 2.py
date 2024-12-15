from itertools import groupby
from collections import defaultdict

input: list[str] = list()

with open("input/day_12_test.txt", "r") as file:
    for line in file:
        input.append([x for x in line.rstrip()])


def plantAreas(plant: str, pos: tuple[int,int], field: list[str], direction: str) -> tuple[int,set[tuple[int,int]],set[tuple[int,int,str]]]:
    pos_y, pos_x = pos

    if not pos_y in range(0, len(field)) or not pos_x in range(0, len(field)):
        return (0,{},{(pos_y, pos_x, direction)}) #area, pos_set, border_set
    
    if '#' == field[pos_y][pos_x]:
        return (0,{},{}) #area, pos_set, border_set
        
    if plant != field[pos_y][pos_x]:
        return (0,{},{(pos_y, pos_x, direction)}) #area, pos_set, border_set
        

    new_pos = [(pos_y+dy,pos_x+dx) for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]]

    new_pos_v = [(pos_y+dy,pos_x+dx) for dy, dx in [(0,1), (0,-1)]]
    new_pos_h = [(pos_y+dy,pos_x+dx) for dy, dx in [(1,0), (-1,0)]]

    field[pos_y][pos_x] = '#'

    area = 1
    pos_set = {pos}
    border_set = set()

    for new in new_pos_v:
        darea, dpos_set, dborder_set = plantAreas(plant, new, field, '|')
        area += darea
        pos_set = pos_set.union(dpos_set)
        border_set = border_set.union(dborder_set)
        #print(dborder_set, border_set)
    for new in new_pos_h:
        darea, dpos_set, dborder_set = plantAreas(plant, new, field, '-')
        area += darea
        pos_set = pos_set.union(dpos_set)
        border_set = border_set.union(dborder_set)

    return (area, pos_set, border_set)

def detect_range(pos: list[int]):
    for i, j in groupby(enumerate(pos), lambda x: x[1] - x[0]):
        j = list(j)
        yield j[0][1], j[-1][1]

area, pos_set, border_set = plantAreas('R', (0,0), input, '')

groups = defaultdict(list)

#print(border_set)

sideborders = list()
topbotborders = list()

for border in border_set:
    groups[border[2]].append(border)
    y, x, b_type = border
    if b_type == '|':
        sideborders.append((y,x))
    if b_type == '-':
        topbotborders.append((y,x))

print(dict(groups))

sorted_sides = sorted(sideborders, key=lambda x: (x[1], x[0]))
sorted_topbot = sorted(topbotborders)

[x for _, xs in groupby(sorted_sides, lambda x: x[1]) for x in xs]

grouped_sides = [list(x) for _, x in groupby(sorted_sides, lambda x: x[1])] #list(groupby(sorted_sides, lambda x: x[1]))
grouped_topbot = [list(x) for _,x in groupby(sorted_topbot, lambda x: x[0])] #list(groupby(sorted_topbot, lambda x: x[0]))

print(grouped_sides)
print(grouped_topbot)


#print(sorted(sideborders, key=lambda x: (x[1], x[0])))
#print(sorted(topbotborders))

#test = groupby(sorted(sideborders, key=lambda x: (x[1], x[0])), lambda x: x[1])
#for k,g in test:
#    print(k, list(detect_range([y for y,_ in list(g)])))
    
#something = [list(detect_range([y for y,_ in list(g)])) for _,g in groupby(sorted(sideborders, key=lambda x: (x[1], x[0])), lambda x: x[1])]
#print(something)

#flat_list = [
#    x
#    for xs in something
#    for x in xs
#]

#print(flat_list)

#sideborders = list(detect_range([y for y,_ in sorted(sideborders, key=lambda x: (x[1], x[0]))]))
#topbotborders = list(detect_range([x for _,x in sorted(topbotborders)]))
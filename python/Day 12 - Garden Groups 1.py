input: list[str] = list()

with open("input/day_12_test.txt", "r") as file:
    for line in file:
        input.append([x for x in line.rstrip()])

def areaSearch(exploration_list: list[tuple[str, tuple[int,int]]], field: list[str]) -> list[int]:

    output = list()

    area = 0
    border = 0

    dp = [(1,0), (0,1), (-1,0), (0,-1)]

    current_plant, _ = exploration_list[0]

    while exploration_list:
        next_position = next(((plant, (pos_y, pos_x)) for plant, (pos_y, pos_x) in exploration_list if plant == current_plant), None)
        if next_position == None:
            output.append((current_plant, area, border))
            area = 0
            border = 0
            next_position = next((plant, (pos_y, pos_x)) for plant, (pos_y, pos_x) in exploration_list)
            current_plant, _ = next_position

        exploration_list.remove(next_position)
        
        plant, (pos_y, pos_x) = next_position

        area += 1
        for dy, dx in dp:
            if not (pos_y+dy in range(0, len(field)) and pos_x+dx in range(0, len(field))):
                border += 1
                continue

            plant = field[pos_y+dy][pos_x+dx]
            if plant == '.':
                continue
            
            if (plant, (pos_y+dy, pos_x+dx)) in exploration_list:
                border += 1
                continue
            
            exploration_list.append((plant, (pos_y+dy, pos_x+dx)))

            if plant != current_plant:
                border += 1
        
        field[pos_y][pos_x] = '.'

        print(next_position, area, border)
        print(exploration_list)

    return output

print(areaSearch([('R', (0,0))], input))

plant_pos: dict[str:list[tuple[int,int]]] = dict()

for row, line in enumerate(input):
    for column, plant in enumerate(line):
        if plant in plant_pos:
            plant_pos[plant].append((row,column))
        else:
            plant_pos[plant] = [(row,column)]

#print(plant_pos["I"])

plant_line = dict()

#for key in plant_pos:
#    for pos_y, pos_x in plant_pos[key]:
#        plant_line[pos_y] =
#        pass
#    pass

#def arearecurtion(pos_list: list[tuple[int,int]]) -> tuple[list[dict[str: int]], list[tuple[int,int]]]:
#
#
#    dp = [(1,0), (0,1), (-1,0), (0,-1)]
#    sy, sx = pos_list.pop(0)
#
#    for dy, dx in dp:
#
#        pass
#
#    return
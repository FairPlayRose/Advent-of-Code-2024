input = ''

with open("input/day_15.txt", "r") as file:
        input = input.join(file)

warehouse, path = input.split('\n\n')

warehouse = [[x for x in line] for line in warehouse.split('\n')]
path = ''.join(path.split('\n'))
robot = (0,0)

for row, line in enumerate(warehouse):
    for column, item in enumerate(line):
        if item == '@':
            robot = (row, column)    
        
#for line in warehouse:
#    print(line)
#print(robot)
#print(path)
#print(len(path))

def move_list(direction: tuple[int,int], start: tuple[int,int], warehouse: list[list[str]]) -> list[tuple[int,int]] | None:
    dy, dx = direction
    sy, sx = start
    
    if warehouse[sy+dy][sx+dx] == "#":
        return None
    if warehouse[sy+dy][sx+dx] == '.':
        return [(sy+dy,sx+dx)]
    
    moves = move_list(direction, (sy+dy,sx+dx), warehouse)
    
    if moves == None:
        return None
    
    moves.append((sy+dy,sx+dx))
    
    return moves

direction = (0,0)

for move in path:
    match move:
        case '^': direction = (-1, 0)
        case 'v': direction = (1, 0)
        case '<': direction = (0, -1)
        case '>': direction = (0, 1)
    
    moves = move_list(direction, robot, warehouse)
    
    if moves == None:
        continue
    
    #print(moves)
    #for line in warehouse:
    #    print(line)
    
    new_robot_y, new_robot_x = moves[-1]
    warehouse[new_robot_y][new_robot_x] = '@'
    old_robot_y, old_robot_x = robot
    warehouse[old_robot_y][old_robot_x] = '.'
    
    robot = (new_robot_y, new_robot_x)
    
    for move_y, move_x in moves[:-1]:
        warehouse[move_y][move_x] = 'O'
        
#for line in warehouse:
#    print(line)
    
checksum = 0
    
for row, line in enumerate(warehouse):
    for column, item in enumerate(line):
        if item == 'O':
            checksum += row * 100 + column

print(checksum)
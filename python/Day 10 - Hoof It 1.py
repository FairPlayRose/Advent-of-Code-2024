input = list()

with open("input/day_10.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

def valid_paths(step: int, position: tuple[int,int], map: list[str]) -> set[tuple[int,int]]:

    if step == 9:
        return {position}
    
    py, px = position

    dp_list = [(1,0), (0,1), (-1,0), (0, -1)]
    
    new_positions = [(py+dy,px+dx) 
                     for dy, dx in dp_list 
                     if py+dy in range(0,len(map))
                         and px+dx in range(0, len(map)) 
                         and int(map[py+dy][px+dx]) == step + 1]

    new_position_set = set()

    for new_pos in new_positions:
        new_position_set.update(valid_paths(step + 1, new_pos, map))

    return new_position_set

input_zeros = [(y,x) 
               for y, line in enumerate(input)
               for x, height in enumerate(line)
               if height == '0']

output = sum([len(valid_paths(0, (y,x), input)) for y, x in input_zeros])

print(output)
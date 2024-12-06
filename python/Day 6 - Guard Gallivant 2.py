input = list()

with open("input/day_06.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

def replacer(index: int, character: str, string: str):
    out = string[:index] + character + string[index+1:]
    return out

map_size = len(input)
guard = (-1,-1)

for i, row in enumerate(input):
    for j, column in enumerate(row):
        if '^' == column:
            guard = (i,j)
            input[i] = replacer(j, "X", input[i])

direction = 'up'

guard_path = list()
guard_path.append((guard, direction))
block_counter = 0

while direction != 'gone':
    (i,j) = guard
    
    match direction:
        case 'up':
            for i_ in reversed(range(i)):
                if input[i_][j] == '#':
                    guard = (i_ + 1, j)
                    direction = 'right'
                    break
                else:
                    input[i_] = replacer(j, 'X', input[i_])

            if direction == 'up':
                direction = 'gone'
                
        case 'right':
            for j_ in range(j+1, map_size):
                if input[i][j_] == '#':
                    guard = (i, j_ - 1)
                    direction = 'down'
                    break
                else:
                    input[i] = replacer(j_, 'X', input[i])
            if direction == 'right':
                direction = 'gone'
        
        case 'down':
            for i_ in range(i+1, map_size):
                if input[i_][j] == '#':
                    guard = (i_ - 1, j)
                    direction = 'left'
                    break
                else:
                    input[i_] = replacer(j, 'X', input[i_])
            if direction == 'down':
                direction = 'gone'
        
        case 'left':
            for j_ in reversed(range(j)):
                if input[i][j_] == '#':
                    guard = (i, j_ + 1)
                    direction = 'up'
                    break
                else:
                    input[i] = replacer(j_, 'X', input[i])
            if direction == 'left':
                direction = 'gone'
    
    guard_path.append((guard, direction))
    last_3_guard_pos = guard_path[-3:]
    #print(last_3_guard_pos)

    if len(last_3_guard_pos) == 3:
        last_4_guard_pos = list()

        #print(last_3_guard_pos)

        # error here
        match last_3_guard_pos:
            case [((ty, tx), 'down'), ((sy, sx), 'left'), ((ly, lx), 'up')]:
                virtual = ((ty, lx), 'right')
                last_3_guard_pos = [virtual, ((ty, tx), 'down'), ((sy, sx), 'left'), ((ly, lx), 'up')]

            case [((ty, tx), 'left'), ((sy, sx), 'up'), ((ly, lx), 'right')]:
                virtual = ((ly, tx), 'down')
                last_3_guard_pos = [((ly, lx), 'right'), virtual, ((ty, tx), 'left'), ((sy, sx), 'up')]

            case [((ty, tx), 'up'), ((sy, sx), 'right'), ((ly, lx), 'down')]:
                virtual = ((ty, lx), 'left')
                last_3_guard_pos = [((sy, sx), 'right'), ((ly, lx), 'down'), virtual, ((ty, tx), 'up')]

            case [((ty, tx), 'right'), ((sy, sx), 'down'), ((ly, lx), 'left')]:
                virtual = ((ly, tx), 'up')
                last_3_guard_pos = [((ty, tx), 'right'), ((sy, sx), 'down'), ((ly, lx), 'left'), virtual]
            
            case [_, _, (_, 'gone')]:
                continue

            case _:
                print('PANIC')

        #print(last_3_guard_pos)
        ((tl_y,tl_x),_), ((tr_y, tr_x),_), ((br_y,br_x),_), ((bl_y, bl_x),_) = last_3_guard_pos

        top_line = [(input[tl_y][i] == '.' or input[tl_y][i] == 'X') for i in range(tl_x, tr_x + 1)] #Doing: top_line Range: range(tl_x, tr_x + 1) Fix: tl_y
        right_line = [(input[i][tr_x] == '.' or input[i][tr_x] == 'X') for i in range(tr_y, br_y + 1)] #Doing: right_line Range: range(tr_y, br_y + 1) Fix: tr_x 
        bottom_line = [(input[br_y][i] == '.' or input[br_y][i] == 'X') for i in range(tl_x, tr_x + 1)] #Doing: bottom_line Range: range(tl_x, tr_x + 1) Fix: br_y
        left_line = [(input[i][tl_x] == '.' or input[i][tl_x] == 'X') for i in range(tr_y, br_y + 1)] #Doing: left_line Range: range(tr_y, br_y + 1) Fix: tl_x
        
        if 43 > block_counter > 40:
            print(block_counter)
            print(all(right_line + left_line + top_line + bottom_line))

        if not all(right_line + left_line + top_line + bottom_line):
            # (tr_y,tr_x + 1), (br_y + 1, br_x), (bl_y,bl_x - 1), (tl_y - 1, tl_x)
            continue

        print(guard)
        overline = ""
        if 42 > block_counter > 40:
            for i in range(130):
                if i % 5 == 0:
                    overline += '*'
                else:
                    overline += '|'
            
            print(overline)
            
            for n, line in enumerate(input):
                print(line, " ", n)
        
        tr_blocked = (input[tr_y][tr_x + 1] == '.' or input[tr_y][tr_x + 1] == '#')
        br_blocked = (input[br_y + 1][br_x] == '.' or input[br_y + 1][br_x] == '#')
        bl_blocked = (input[bl_y][bl_x - 1] == '.' or input[bl_y][bl_x - 1] == '#')
        tl_blocked = (input[tl_y - 1][tl_x] == '.' or input[tl_y - 1][tl_x] == '#')

        print(tr_blocked, br_blocked, bl_blocked, tl_blocked)

        if not all([tr_blocked, br_blocked, bl_blocked, tl_blocked]):
            #print('here')
            continue

        block_counter += 1 
        #print(block_counter)  
        
    #print(direction)
    #for line in input:
    #    print(line)
    #print('\n')


#counter = 0
#for row in input:
#    for column in row:
#        if column == 'X':
#            counter += 1
#
#print(counter)
    
print(block_counter)
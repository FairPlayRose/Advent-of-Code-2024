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

direction = 'up'
i,j = guard

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
    
    #print(direction)
    #for line in input:
    #    print(line)
    #print('\n')

#for n, line in enumerate(input):
#    print(line, " ", n)

counter = 0
for row in input:
    for column in row:
        if column == 'X' or column == "^":
            counter += 1

print(counter)
    
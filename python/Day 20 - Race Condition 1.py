input: list[list[str]] = list()

with open("input/day_20.txt", "r") as file:
    for line in file:
        input.append([x for x in line.rstrip()])
        
path: list[tuple[int, int]] = list()
start: tuple[int,int] = (0,0)
end = (0,0)
        
for y, row in enumerate(input):
    for x, column in enumerate(row):
        if column == '.':
            path.append((y,x))
        if column == 'S':
            start = (y,x)
            input[y][x] = '.'
        if column == 'E':
            path.append((y,x))
            input[y][x] = '.'

prev = start
current = start

ordered_path = [start]

dp = [(1,0), (0,1), (-1,0), (0,-1)]

while path:
    for dy, dx in dp:
        cur_y, cur_x = current
        if (cur_y+dy,cur_x+dx) in path and (cur_y+dy,cur_x+dx) != prev:
            prev = current
            current = (cur_y+dy,cur_x+dx)
            ordered_path.append(current)
            path.remove((cur_y+dy,cur_x+dx))

#print('Done')

cheat_path_lens = list()

#for row in input[1:-1]:
#    print(row[1:-1])

for i, row in enumerate(input[1:-1]):
    for j, column in enumerate(row[1:-1]):
        if column != '#': continue
        #print(column, (i+1,j+1))
        if input[i][j+1] == '.' and input[i+2][j+1] =='.':
            jump1, jump2 = sorted([ordered_path.index((i,j+1)),ordered_path.index((i+2,j+1))])
            path_with_cheat = ordered_path[:jump1] + [(i+1,j+1)] + ordered_path[jump2:]
            cheat_path_lens.append(len(ordered_path)-len(path_with_cheat))
        elif input[i+1][j] == '.' and input[i+1][j+2] == '.':
            jump1, jump2 = sorted([ordered_path.index((i+1,j)),ordered_path.index((i+1,j+2))])
            path_with_cheat = ordered_path[:jump1] + [(i+1,j+1)] + ordered_path[jump2:]
            cheat_path_lens.append(len(ordered_path)-len(path_with_cheat))
    
print(sum([100 <= cheat_path for cheat_path in cheat_path_lens]))
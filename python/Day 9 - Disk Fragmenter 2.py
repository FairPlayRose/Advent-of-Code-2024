input = list()

with open("input/day_09.txt", "r") as file:
    for line in file:
        input.append(line.rstrip())

input = input[0]

data = [[int(file), i//2] for i, file in enumerate(input) if i % 2 == 0]
space = [int(gap) for i, gap in enumerate(input) if i % 2 == 1] + [0]

data_index = len(data) - 1
start_space_index = 0

#print(data)
#print([file[0] for file in data], data_index)
#print(space, start_space_index)
#print('')

while start_space_index < data_index:
    space_copy = space.copy()

    for i in range(start_space_index, data_index):

        file = data[data_index]

        if file[0] <= space_copy[i]:
            space = space[0:i] + [0, space[i] - file[0]] + space[i+1:data_index-1] + [file[0] + space[data_index-1] + space[data_index]] + space[data_index+1:]
            data = data[0:i+1] + [data[data_index]] + data[i+1:data_index] + data[data_index+1:]
            data_index += 1
            break

    data_index -= 1
    for i, gap in enumerate(space):
        if gap == 0:
            continue
        start_space_index = i
        break
    
    #print(data)
    #print([file[0] for file in data], data_index)
    #print(space, start_space_index)
    #print('')

space = [0] + space[:-1]

#print(data)
#print([file[0] for file in data], data_index)
#print(space, start_space_index)

position = 0
check_sum = 0

for index, [file_space, file_index] in enumerate(data):
    position += space[index]
    for i in range(position, position + file_space):
        check_sum += i*file_index
    position += file_space

print(check_sum)
import itertools

items: list[str]

with open("input/day_25.txt", "r") as file:
    items = file.read().split('\n\n')

keys: list[list[str]] = list()
locks: list[list[str]] = list()

for item in items:
    lines = item.split('\n')
    _item = [''.join(s) for s in zip(*lines)]
    #print(_item)
    if lines[0] == '#####':
        locks.append(_item)
    elif lines[0] == '.....':
        keys.append(_item)


keys = [[len(list(group)) - 1 for column in key for k, group in itertools.groupby(column)][::2] for key in keys]
locks = [[len(list(group)) - 1 for column in lock for k, group in itertools.groupby(column)][::2] for lock in locks]

#print(keys)
#print(locks)
            
checksum = sum([all([(int(k) >= int(l)) for k, l in zip(key,lock)]) for key in keys for lock in locks])

print(checksum)




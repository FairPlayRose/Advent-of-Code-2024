from collections import Counter

input1 = list()
input2 = list()

with open("input/day_01.txt", "r") as file:
    for line in file:
        entries = line.rstrip().split("   ")
        input1.append(entries[0])
        input2.append(entries[1])

dict1 = dict(Counter(input1))
dict2 = dict(Counter(input2))

sim_score = sum([int(key) * int(value) * dict2.get(key,0) for key, value in dict1.items()])

print(sim_score)
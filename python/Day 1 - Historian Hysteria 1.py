
input1 = list()
input2 = list()

with open("input/day_01.txt", "r") as file:
    for line in file:
        entries = line.rstrip().split("   ")
        input1.append(entries[0])
        input2.append(entries[1])

input1.sort()
input2.sort()

total_dist = sum([abs(int(a)-int(b)) for a,b in zip(input1,input2)])

print(total_dist)
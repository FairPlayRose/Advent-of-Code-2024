input: list[int] = list()

with open("input/day_22.txt", "r") as file:
    for line in file:
        input.append(int(line.rstrip()))
        
def next_number_step(number: int) -> int:
    first = ((number << 6) ^ number) % 16777216
    second = ((first >> 5) ^ first) % 16777216
    return ((second << 11) ^ second) % 16777216

checksum = 0

for number in input:
    for _ in range(2000):
        number = next_number_step(number)
    checksum += number
    #print(number)
#test_1 = ((number << 12) ^ (number << 15) ^ (number << 11) ^ number ^ (number << 1) ^ (number >> 5)) % 16777216

print(checksum)
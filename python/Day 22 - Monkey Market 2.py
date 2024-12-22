input: list[int] = list()

with open("input/day_22.txt", "r") as file:
    for line in file:
        input.append(int(line.rstrip()))
        
def next_number_step(number: int) -> int:
    first = ((number << 6) ^ number) % 16777216
    second = ((first >> 5) ^ first) % 16777216
    third = ((second << 11) ^ second) % 16777216
    return (third, third % 10 - number % 10)

change_lists: list[list[int]] = list()

for number in input:
    change_list: list[int] = list()
    for _ in range(2000):
        number, change = next_number_step(number)
        change_list.append(change)
    change_lists.append(change_list)


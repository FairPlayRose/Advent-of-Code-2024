input_rules = list()
input_updates = list()

with open("input/day_05.txt", "r") as file:
    for line in file:
        stripline = line.rstrip()
        if len(stripline) == 5:
            input_rules.append(stripline)
        elif len(stripline) == 0:
            pass
        else:
            input_updates.append(stripline)

output = list()

for updates in input_updates:
    update_list = updates.split(",")

    middle_update_index = len(update_list)//2
    fine_updates = list()
    is_updates_fine = True

    fine_updates.append(update_list[::-1][0])

    for update in update_list[-2::-1]:
        for fines in fine_updates:

            rules_test = f'{update}|{fines}'

            if not rules_test in input_rules:
                is_updates_fine = False
        
        if is_updates_fine:
            fine_updates.append(update)

    if is_updates_fine:
        output.append(int(update_list[middle_update_index]))

print(sum(output))
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
bad_updates = list()

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
    else:
        bad_updates.append(update_list)


# Implemeted recursive merge_sort for rules
def rules_merge_sort(rules: list[str], updates: list[str]) -> list[str]:
    right_list = list()
    left_list = list()

    if len(updates) <= 1:
        return updates
    
    updates_mid_index = len(updates)//2
    item = updates[updates_mid_index]
    
    for update in updates:
        match update:
            case update if f'{update}|{item}' in rules: left_list.append(update)
            case update if f'{item}|{update}' in rules: right_list.append(update)

    return rules_merge_sort(rules, left_list) + [item] + rules_merge_sort(rules, right_list)


output_2 = list()

for bad_update in bad_updates:
    sorted_bad = rules_merge_sort(input_rules, bad_update)
    #print("Before: ", bad_update, "After: ", sorted_bad)
    sorted_mid_index = len(sorted_bad)//2
    output_2.append(int(sorted_bad[sorted_mid_index]))

print(sum(output_2))


def fully_contains(lines):
    overlaps = 0
    for line in lines:
        line = line.strip()
        pair = line.split(',')
        pair_1_ints = pair[0].split('-')
        pair_1_ints = [eval(i) for i in pair_1_ints]
        pair_2_ints = pair[1].split('-')
        pair_2_ints = [eval(i) for i in pair_2_ints]
        if (pair_1_ints[0] >= pair_2_ints[0] and pair_1_ints[1] <= pair_2_ints[1] or
            pair_2_ints[0] >= pair_1_ints[0] and pair_2_ints[1] <= pair_1_ints[1]):
            overlaps += 1
    return overlaps

def some_overlap(lines):
    overlaps = 0
    for line in lines:
        line = line.strip()
        pair = line.split(',')
        pair_1_ints = pair[0].split('-')
        pair_1_ints = [eval(i) for i in pair_1_ints]
        pair_2_ints = pair[1].split('-')
        pair_2_ints = [eval(i) for i in pair_2_ints]
        if (pair_1_ints[1] == pair_2_ints[0] or
                pair_1_ints[0] <= pair_2_ints[0] <= pair_1_ints[1] or
                pair_2_ints[0] <= pair_1_ints[0] <= pair_2_ints[1] or
                pair_1_ints[0] >= pair_2_ints[0] and pair_1_ints[1] <= pair_2_ints[1] or
                pair_2_ints[0] >= pair_1_ints[0] and pair_2_ints[1] <= pair_1_ints[1]):
            overlaps += 1
            print(pair)

        # same thing
    return overlaps

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()
    result = fully_contains(lines)
    print(result)
    result = some_overlap(lines)
    print(result)
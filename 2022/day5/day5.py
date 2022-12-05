def last_box(lines, boxes):
    # follow instructions
    for line in lines:
        line = line.strip()
        moves = line.split(" ")
        print(moves)
        # moves[1] is amount, moves[3] is source, moves[5] is destination
        for i in range(int(moves[1])):
            elem = boxes[int(moves[3]) - 1].pop()
            boxes[int(moves[5]) - 1].append(elem)
        print(boxes)
    # Get the box at the end of each stack
    ends = ""
    for box in boxes:
        ends += box[-1]
    return ends
    
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
    # Do the list processing here
    # Need a few things:
    # Number of lists should be the last number in the first lines that contains numbers
    # Insert boxes through top to bottom as you read
    boxes = []
    stacks = 0
    for line in lines:
        if any(char.isdigit() for char in line):
            stacks = int(line.split()[-1])
            break
        else:
            boxes.append(line)
    # allocate boxes
    newboxes = []
    for i in range(stacks):
        newboxes.append([])
    for line in boxes:
        # Characters always appear within boxes at these intervals
        for i in range(1, len(line), 4):
            if(line[i].isalpha()):
                newboxes[i//4].insert(0, line[i][0])
    result = last_box(lines[stacks + 2:], newboxes)
    print(result)
    # result = some_overlap(lines)
    # print(result)
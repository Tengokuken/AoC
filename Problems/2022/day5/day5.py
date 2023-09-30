def last_box(lines, boxes):
    print(lines)
    # follow instructions
    for line in lines:
        line = line.strip()
        moves = line.split(" ")
        print(moves)
        # moves[1] is amount, moves[3] is source, moves[5] is destination
        print(moves)
        for i in range(int(moves[1])):
            elem = boxes[int(moves[3]) - 1].pop()
            boxes[int(moves[5]) - 1].append(elem)
        print(boxes)
    # Get the box at the end of each stack
    ends = ""
    for box in boxes:
        ends += box[-1]
    return ends

def crate_mover_9001(lines, boxes):
    # follow instructions
    for line in lines:
        line = line.strip()
        moves = line.split(" ")
        # print(moves)
        # moves[1] is amount, moves[3] is source, moves[5] is destination
        # print(moves)
        temp = []
        for i in range(int(moves[1])):
            elem = boxes[int(moves[3]) - 1].pop()
            temp.append(elem)
        for i in range(len(temp)):
            elem = temp.pop()
            boxes[int(moves[5]) - 1].append(elem)
        print(boxes)
    # Get the box at the end of each stack
    ends = ""
    for box in boxes:
        ends += box[-1]
    return ends

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

    # Exclusive since the newboxes change
    # result = last_box(lines[stacks + 1:], newboxes)
    # print(result)
    result = crate_mover_9001(lines[stacks + 1:], newboxes)
    print(result)
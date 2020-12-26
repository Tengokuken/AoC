def check_slope(f, increment, down):
    current_x = 0
    current_y = 0
    num_trees = 0
    for line in f:
        current_y += 1
        if 1 < down == current_y:
            current_y = 0
            continue
        # repeating line of trees
        if current_x + 1 >= len(line):
            current_x = current_x % (len(line) - 1)
        # Check if tree in the way
        if tree(line, current_x):
            num_trees += 1
        current_x += increment
    print(num_trees)
    return num_trees


def tree(line, x_pos):
    print(x_pos)
    if line[x_pos] == '#':
        print(line[:x_pos] + 'X' + line[x_pos + 1:])
    else:
        print(line[:x_pos] + 'O' + line[x_pos + 1:])
    return line[x_pos] == '#'

# Driver code
if __name__ == "__main__":
    with open("input.txt") as f:
        num_trees = check_slope(f, 3, 1)
    with open("input.txt") as f:
        num_trees *= check_slope(f, 1, 1)
    with open("input.txt") as f:
        num_trees *= check_slope(f, 5, 1)
    with open("input.txt") as f:
        num_trees *= check_slope(f, 7, 1)
    with open("input.txt") as f:
        num_trees *= check_slope(f, 1, 2)

    print(num_trees)
    # print(valid_passes_new)
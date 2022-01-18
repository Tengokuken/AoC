def travel(input):
    horizontal = 0
    depth = 0
    for command in input:
        # Get first word, check direction
        command = command.split(' ')
        amount = int(command[1])
        if command[0] == 'forward':
            horizontal += amount
        elif command[0] == 'down':
            depth += amount
        elif command[0] == 'up':
            depth -= amount
    return(horizontal, depth)

def travel2(input):
    horizontal = 0
    depth = 0
    aim = 0
    for command in input:
        # Get first word, check direction
        command = command.split(' ')
        amount = int(command[1])
        if command[0] == 'forward':
            horizontal += amount
            depth += aim * amount
        elif command[0] == 'down':
            aim += amount
        elif command[0] == 'up':
            aim -= amount

    return(horizontal, depth)
# Driver code
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    # lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    positions = travel(lines)
    print(positions)
    print(positions[0] * positions[1])
    positions = travel2(lines)
    print(positions)
    print(positions[0] * positions[1])

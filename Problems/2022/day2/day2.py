def strat(lines):
    # 1 point rock, 2 point paper, 3 points scissors
    # 0 lose, 3 tie, 6 win
    points = 0
    for line in lines:
        l = line.split(" ")
        print(line)
        if l[0] == 'A':
            if l[1] == 'X\n':
                points += 4
            elif l[1] == "Y\n":
                points += 8
            elif l[1] == "Z\n":
                points += 3
        elif l[0] == 'B':
            if l[1] == 'X\n':
                points += 1
            elif l[1] == "Y\n":
                points += 5
            elif l[1] == "Z\n":
                points += 9
        elif l[0] == 'C':
            if l[1] == 'X\n':
                points += 7
            elif l[1] == "Y\n":
                points += 2
            elif l[1] == "Z\n":
                points += 6
    return points


def other_strat(lines):
    # 1 point rock, 2 point paper, 3 points scissors
    # 0 lose, 3 tie, 6 win
    # x means lose, y means draw, z means win
    points = 0
    for line in lines:
        l = line.split(" ")
        print(line)
        if l[0] == 'A':
            if l[1] == 'X\n':
                points += 3
            elif l[1] == "Y\n":
                points += 4
            elif l[1] == "Z\n":
                points += 8
        elif l[0] == 'B':
            if l[1] == 'X\n':
                points += 1
            elif l[1] == "Y\n":
                points += 5
            elif l[1] == "Z\n":
                points += 9
        elif l[0] == 'C':
            if l[1] == 'X\n':
                points += 2
            elif l[1] == "Y\n":
                points += 6
            elif l[1] == "Z\n":
                points += 7
    return points

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()
    result = strat(lines)
    print(result)
    result = other_strat(lines)
    print(result)
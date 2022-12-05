import string
priorities = '\n' + string.ascii_letters # adding the \n to cheat kinda
print(priorities)

def sum_priorities(lines):
    sumpri = 0
    for line in lines:
        # split in half
        first = set(line[:len(line)//2])
        second = set(line[len(line)//2:])
        # find common elements
        common = ''.join(sorted(first.intersection(second)))
        # convert priorities
        for char in common:
            sumpri += priorities.index(char)
    return sumpri

def common_three(lines):
    sumpri = 0
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        # get 3 lines
        first = set(group[0])
        second = set(group[1])
        third = set(group[2])
        common = ''.join(sorted(first.intersection(second.intersection(third))))
        # find common elements in 3 lines
        for char in common:
            sumpri += priorities.index(char)
        # same thing
    return sumpri

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()
    result = sum_priorities(lines)
    print(result)
    result = common_three(lines)
    print(result)
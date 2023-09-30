def sig_start(line):
    # one line
    for i in range(len(line) - 4):
        substr = line[i:i+4]
        if len(substr) == len(set(substr)):
            print(substr)
            return i + 4
    # return

def sig_start2(line):
    # one line
    for i in range(len(line) - 14):
        substr = line[i:i+14]
        if len(substr) == len(set(substr)):
            print(substr)
            return i + 14


if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()

    result = sig_start(lines[0])
    print(result)
    result = sig_start2(lines[0])
    print(result)
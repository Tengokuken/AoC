def execute(lines):
    tick = 0
    reg = 1
    strengths = 0
    six_cycles = [20, 60, 100, 140, 180, 220]
    for i in range(len(lines)):
        tick += 1
        if tick in six_cycles:
            strengths += tick * reg
            print("X:", tick * reg)
        line = lines[i].split(" ")
        if line[0] == "addx":
            tick += 1
            if tick in six_cycles:
                strengths += tick * reg
            reg += int(line[1])
        print("cycle", tick, "val:", reg)

    return strengths

def draw_pixel(tick, row, reg):
    mid = tick % 40

    if not mid:
        row += 1
        print()
    if mid-1 <= reg <= mid+1:
        print("#", end='')
    else:
        print(".", end='')
def images(lines):
    tick = 0
    reg = 1
    row = 0
    for i in range(len(lines)):
        line = lines[i].split(" ")
        if line[0] == "addx":
            # Delay once, draw same pixel
            for _ in range(2):
                draw_pixel(tick, row, reg)
                tick += 1
            reg += int(line[1])
        else:
            draw_pixel(tick, row, reg)
            tick += 1


if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()

    result = execute(lines)
    print(result)
    images(lines)



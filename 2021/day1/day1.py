def count_increase(input):
    count = 0
    prev = input[0]
    for inp in input:
        if inp > prev:
            count += 1
        prev = inp
    return count

def window_increase(input):
    count = 0
    prev_window = sum(input[0:3])
    for i in range(1, len(input) - 2):
        window = sum(input[i:i+3])
        if window > prev_window:
            count += 1
        prev_window = window
    return count


# Driver code
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    lines = [int(i) for i in lines]
    # lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    num_increases = count_increase(lines)
    print(num_increases)
    num_increases = window_increase(lines)
    print(num_increases)

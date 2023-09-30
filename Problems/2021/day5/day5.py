def collide(lines):
    map = []
    collisions = 0
    count = 0
    for line in lines:
        print('processing:', str(count))
        count += 1
        line = line.split(' -> ')
        line.sort()
        start = line[0].split(',')
        end = line[1].split(',')
        start = [int(x) for x in start]
        end = [int(x) for x in end]

        # Vertical
        if start[0] == end[0]:
            ridge = range(start[1], end[1] + 1)
            for i in ridge:
                ridge_point = [start[0], i]
                if ridge_point in map:
                    collisions += 1
                # else:
                map.append(ridge_point)
        elif start[1] == end[1]:
            ridge = range(start[0], end[0] + 1)
            for i in ridge:
                ridge_point = [i, start[1]]
                if ridge_point in map:
                    collisions += 1
                # else:
                map.append(ridge_point)
        # print(map)
    # print(map)
    return collisions

# Driver code
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    # lines = [int(i) for i in lines]
    result = collide(lines)
    print(result)
    result = consume(lines)
    print(result)
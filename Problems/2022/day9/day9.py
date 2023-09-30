import math
locations = set()
# part 1
h = [0, 0]
t = [0, 0]
# part 2
body = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
def move_rope(dir, dist):
    # move head first
    global h
    global t
    for _ in range(dist):
        prev_h = h.copy()
        print("h", h)
        print("t", t)
        if dir == "L":
            h[0] -= 1
        elif dir == "R":
            h[0] += 1
        elif dir == "U":
            h[1] += 1
        elif dir == "D":
            h[1] -= 1
        # if absolute distance between h and t > 1, t needs to move.

        if math.dist(h, t) > math.sqrt(2):
            print("jump here?")
            t = prev_h
        locations.add(tuple(t))

    # for obj in locations:
    #     print(obj)

def move_10_rope(dir, dist):
    # same thing now but with 10 parts
    global body
    for _ in range(dist):
        if dir == "L":
            body[0][0] -= 1
        elif dir == "R":
            body[0][0] += 1
        elif dir == "U":
            body[0][1] += 1
        elif dir == "D":
            body[0][1] -= 1
        # if absolute distance between each adjacent > root 2, next part needs to move.
        for i in range(1, len(body)):
            if math.dist(body[i - 1], body[i]) > math.sqrt(2):
                dist_x = body[i - 1][0] - body[i][0]
                dist_y = body[i - 1][1] - body[i][1]
                if dist_x != 0:
                    body[i][0] += dist_x // abs(dist_x)
                if dist_y != 0:
                    body[i][1] += dist_y // abs(dist_y)
            locations.add(tuple(body[9]))
def unique_visits(lines, part):
    for move in lines:
        move = move.split(" ")
        if part == 1:
            move_rope(move[0], int(move[1]))
        elif part == 2:
            move_10_rope(move[0], int(move[1]))
    return len(locations)


if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()

    result = unique_visits(lines, 2)
    print(result)



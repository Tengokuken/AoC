import string, math

class Node:
    def __init__(self, elem, edge_weights):
        self.elem = elem
        self.edges = edge_weights
        self.parent = None

    def __repr__(self):
        return ("Node: " + str(self.elem) + " edges: " + str(self.edges))

alpha = list(string.ascii_lowercase) # S = a, E = z
char_values = {"S": 0, "E": 25}
for i in range(len(alpha)):
    char_values[alpha[i]] = i

def check_walkable(curr, neighbour):
    return math.fabs(char_values[curr.elem] - char_values[neighbour.elem]) <= 1

def update_dist(neighbour, dist):
    if neighbour.dist > dist + 1:
        neighbour.dist = dist + 1
def shortest_path_old(graph, start, dest):
    visited = set()
    to_visit = [] # stores a list of coordinates to visit
    # do dijkstras
    to_visit.append(start)
    while to_visit:
        coords = to_visit.pop(0)
        i, j = coords
        print("now on", i, j)
        curr = graph[i][j]
        # Check if neighbours are reachable. If the difference between the indices are 1, then it is reachable.
        # # cases for nesw direction. -1 means not reachable
        if i > 0 and coords not in visited and check_walkable(curr, graph[i - 1][j]):
            curr.edges[0] = 1
            to_visit.append((i - 1, j))
            update_dist(graph[i - 1][j], curr.dist)
        if j < len(lines) - 1 and coords not in visited and check_walkable(curr, graph[i][j + 1]):
            curr.edges[1] = 1
            to_visit.append((i, j + 1))
            update_dist(graph[i][j + 1], curr.dist)
        if i < len(lines) - 1 and coords not in visited and check_walkable(curr, graph[i + 1][j]):
            curr.edges[2] = 1
            to_visit.append((i + 1, j))
            update_dist(graph[i + 1][j], curr.dist)
        if j > 0 and coords not in visited and check_walkable(curr, graph[i][j - 1]):
            curr.edges[3] = 1
            to_visit.append((i, j - 1))
            update_dist(graph[i][j - 1], curr.dist)
        visited.add((i, j))
    print(graph)

def shortest_path(graph, start, dest):
    # do bfs
    to_visit = []  # stores a list of coordinates to visit
    to_visit.append(start)
    visited = set()
    steps = 0
    while to_visit:
        coords = to_visit.pop(0)
        i, j = coords
        print("now on", i, j)
        curr = graph[i][j]
        # Check if neighbours are reachable. If the difference between the indices are 1, then it is reachable.
        # # cases for nesw direction. -1 means not reachable
        if i > 0 and (i - 1, j) not in visited and check_walkable(curr, graph[i - 1][j]):
            curr.edges[0] = 1
            to_visit.append((i - 1, j))
            graph[i - 1][j].parent = curr
        if j < len(lines) - 1 and (i, j + 1) not in visited and check_walkable(curr, graph[i][j + 1]):
            curr.edges[1] = 1
            to_visit.append((i, j + 1))
            graph[i][j + 1].parent = curr
        if i < len(lines) - 1 and (i + 1, j) not in visited and check_walkable(curr, graph[i + 1][j]):
            curr.edges[2] = 1
            to_visit.append((i + 1, j))
            graph[i + 1][j].parent = curr
        if j > 0 and (i, j - 1) not in visited and check_walkable(curr, graph[i][j - 1]):
            curr.edges[3] = 1
            to_visit.append((i, j - 1))
            graph[i][j - 1].parent = curr
        visited.add((i, j))

    print(graph)


## TODO: this is dijkstras btw find path from S to E with the smallest edge weight
if __name__ == "__main__":
    file = open('test.txt', 'r')
    lines = file.readlines()
    file.close()

    # Create a graph of nodes, having an edge to each neighbour
    graph = [[{} for i in range(len(lines[0]) - 1)] for j in range(len(lines))]
    temp_lines = []
    for line in lines:
        line = line.strip('\n')
        temp_lines.append(line)
    lines = temp_lines
    start = (-1, -1)
    end = (-1, -1)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            node_edges = [-1, -1, -1, -1]
            node = Node(lines[i][j], node_edges)
            # Get start and dest nodes
            if lines[i][j] == "S":
                start = (i, j)
                node.dist = 0
            elif lines[i][j] == "E":
                dest = (i, j)
            graph[i][j] = node
    print(graph)
    print(start)
    print(dest)
    result = shortest_path(graph, start, dest)

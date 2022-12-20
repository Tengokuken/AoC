class Node:
    def __init__(self, elem, edges, is_visible):
        self.elem = elem
        self.edges = edges
        self.is_visible = is_visible
        self.score = [0, 0, 0, 0]

    def __repr__(self):
        # return ("Node: " + str(self.elem) + ", edges: " + str(self.edges) + ", visible: " + str(self.is_visible))
        return str(self.is_visible)

def neighbours_visible(graph, x, y):
    # Check if this current tree can see the end of the forest at any of its sides
    loop_visible = True
    # north
    cur_x = x - 1
    while cur_x >= 0:
        if graph[x][y].elem <= graph[cur_x][y].elem:
            loop_visible = False
            break
        cur_x -= 1

    if loop_visible:
        return loop_visible

    loop_visible = True
    cur_y = y + 1
    while cur_y <= len(graph) - 1:
        if graph[x][y].elem <= graph[x][cur_y].elem:
            loop_visible = False
            break
        cur_y += 1

    if loop_visible:
        return loop_visible

    loop_visible = True
    cur_x = x + 1
    while cur_x <= len(graph) - 1:
        if graph[x][y].elem <= graph[cur_x][y].elem:
            loop_visible = False
            break
        cur_x += 1

    if loop_visible:
        return loop_visible

    loop_visible = True
    cur_y = y - 1
    while cur_y >= 0:
        if graph[x][y].elem <= graph[x][cur_y].elem:
            loop_visible = False
            break
        cur_y -= 1

    if loop_visible:
        return loop_visible

    return loop_visible

def num_neighbours_visible(graph, x, y):
    # Check if this current tree can see the end of the forest at any of its sides
    # north
    cur_x = x - 1
    count = 0
    while cur_x >= 0:
        count += 1
        if graph[x][y].elem <= graph[cur_x][y].elem:
            break
        cur_x -= 1

    graph[x][y].score[0] = count

    cur_y = y + 1
    count = 0
    while cur_y <= len(graph) - 1:
        count += 1
        if graph[x][y].elem <= graph[x][cur_y].elem:
            break
        cur_y += 1

    graph[x][y].score[1] = count

    cur_x = x + 1
    count = 0
    while cur_x <= len(graph) - 1:
        count += 1
        if graph[x][y].elem <= graph[cur_x][y].elem:
            break
        cur_x += 1

    graph[x][y].score[2] = count

    cur_y = y - 1
    count = 0
    while cur_y >= 0:
        count += 1
        if graph[x][y].elem <= graph[x][cur_y].elem:
            break
        cur_y -= 1

    graph[x][y].score[3] = count

# This doesn't work but I like that I made a dp solution!!!!!
# Because ie if north visible from west it doesnt mean that this is visible from north
def dp_neighbours_visible(graph, x, y):
    # Given a node, check if the neighbours are visible recursively.
    # Base case: If neighbours are visible and this tree is taller, return True
    if graph[x - 1][y].is_visible and graph[x][y].elem > graph[x - 1][y].elem or \
            graph[x][y + 1].is_visible and graph[x][y].elem > graph[x][y + 1].elem or \
            graph[x + 1][y].is_visible and graph[x][y].elem > graph[x + 1][y].elem or \
            graph[x][y - 1].is_visible and graph[x][y].elem > graph[x][y - 1].elem:
        return True
    # Recursive step: Check north, then east, then south, then west.
    if graph[x][y].elem > graph[x-1][y].elem and dp_neighbours_visible(graph, x - 1, y):
        return True
    if graph[x][y].elem > graph[x][y+1].elem and dp_neighbours_visible(graph, x, y+1):
        return True
    if graph[x][y].elem > graph[x + 1][y].elem and dp_neighbours_visible(graph, x + 1, y):
        return True
    if graph[x][y].elem > graph[x][y-1].elem and dp_neighbours_visible(graph, x, y-1):
        return True
    return False


def visible_trees(graph):
    # Consider the inner trees only
    for i in range(1, len(graph) - 1):
        for j in range(1, len(graph[i]) - 1):
            graph[i][j].is_visible = neighbours_visible(graph, i, j)

    # Traverse through all inner nodes to see what is visible
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (graph[i][j].is_visible):
                count += 1
    return count

def num_visible_trees(graph):
    # Consider the inner trees only
    highest = 0
    for i in range(1, len(graph) - 1):
        for j in range(1, len(graph[i]) - 1):
            num_neighbours_visible(graph, i, j)
            res = 1
            for k in range(4):
                res *= graph[i][j].score[k]
            if res >= highest:
                highest = res
    return highest

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()

    # Create a graph of nodes, having an edge to each neighbour
    graph = [[{} for i in range(len(lines))] for j in range(len(lines))]
    temp_lines = []
    for line in lines:
        line = line.strip('\n')
        temp_lines.append(line)
    lines = temp_lines
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            node_edges = [-1, -1, -1, -1]
            visible = True if i == 0 or j == 0 or i == len(lines) - 1 or j == len(lines) - 1 else False
            # cases for nesw direction. -1 means dne
            if i > 0:
                node_edges[0] = int(lines[i - 1][j])
            if j < len(lines) - 1:
                node_edges[1] = int(lines[i][j + 1])
            if i < len(lines) - 1:
                node_edges[2] = int(lines[i + 1][j])
            if j > 0:
                node_edges[3] = int(lines[i][j - 1])
            node = Node(lines[i][j], node_edges, visible)
            graph[i][j] = node
    # result = visible_trees(graph)
    # print(result)
    result = num_visible_trees(graph)
    print(result)

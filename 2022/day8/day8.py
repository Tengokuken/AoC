class Node:
    def __init__(self, elem, edges, is_visible):
        self.elem = elem
        self.edges = edges
        self.is_visible = is_visible

    def __repr__(self):
        return ("Node: " + str(self.elem) + ", edges: " + str(self.edges) + ", visible: " + str(self.is_visible))


def neighbours_visible(graph, x, y):
    # Check neighbours recursively
    if rec_neighbours_visible(graph, x, y, "n") or \
            rec_neighbours_visible(graph, x, y, "e") or \
            rec_neighbours_visible(graph, x, y, "s") or \
            rec_neighbours_visible(graph, x, y, "w"):
        return True
    return False

def rec_neighbours_visible(graph, x, y, dir):
    # Base case: we are at the edge of the desired direction. Return true
    # Recursive step: Check the tree in the desired direction. Return true if you can see it from this direction
    if dir == "n":
        if x == 0:
            return True
        else:
            return rec_neighbours_visible(graph, x-1, y, "n") and graph[x][y].elem > graph[x-1][y].elem
    if dir == "e":
        if y == len(graph) - 1:
            return True
        else:
            return rec_neighbours_visible(graph, x, y+1, "e") and graph[x][y].elem > graph[x][y+1].elem
    if dir == "s":
        if x == len(graph) - 1:
            return True
        else:
            return rec_neighbours_visible(graph, x+1, y, "s") and graph[x][y].elem > graph[x-1][y].elem
    if dir == "w":
        if y == 0:
            return True
        else:
            return rec_neighbours_visible(graph, x, y-1, "w") and graph[x][y].elem > graph[x][y-1].elem

# This doesn't work but I like that I made a dp solution!!!!!
# Because ie if north visible from west it doesnt mean that this is visible from north
def dp_neighbours_visible(graph, x, y):
    print("At dp step elem", graph[x][y].elem, "at", x, y)
    # Given a node, check if the neighbours are visible recursively.
    # Base case: If neighbours are visible and this tree is taller, return True
    if graph[x - 1][y].is_visible and graph[x][y].elem > graph[x - 1][y].elem or \
            graph[x][y + 1].is_visible and graph[x][y].elem > graph[x][y + 1].elem or \
            graph[x + 1][y].is_visible and graph[x][y].elem > graph[x + 1][y].elem or \
            graph[x][y - 1].is_visible and graph[x][y].elem > graph[x][y - 1].elem:
        print("True because larger than visible neighbours")
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
        print(graph[i])
        for j in range(len(graph[i])):
            if (graph[i][j].is_visible):
                count += 1
    return count


# def sig_start2(graph):
#     # one line
#     for i in range(len(line) - 14):
#         substr = line[i:i+14]
#         if len(substr) == len(set(substr)):
#             print(substr)
#             return i + 14


if __name__ == "__main__":
    file = open('test.txt', 'r')
    lines = file.readlines()
    file.close()

    # Create a graph of nodes, having an edge to each neighbour
    graph = [[{} for i in range(len(lines))] for j in range(len(lines))]
    print(lines)
    temp_lines = []
    for line in lines:
        line = line.strip('\n')
        temp_lines.append(line)
    lines = temp_lines
    print(lines)
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
    print(graph)
    result = visible_trees(graph)
    print(result)
    # result = sig_start2(lines[0])
    print(result)

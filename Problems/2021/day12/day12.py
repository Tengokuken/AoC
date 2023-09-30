import os
# Using a Python dictionary to act as an adjacency list
graph = {
    
}

visited = set() # Set to keep track of visited nodes.
def gen_graph(lines):
    for line in lines:
        line = line.split('-')
        graph[line[0]] = line[1]
    print(graph)

def paths(lines):
    # Create graph
    gen_graph(lines)

    dfs(visited, graph, graph['start'])

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
if __name__ == "__main__":
    print(os.getcwd())
    with open("test1.txt") as f:
        lines = f.read().splitlines()
    score = paths(lines)
    print(score)
    numbers = incomplete(lines)
    print(numbers)
    dfs(visited, graph, 'A')
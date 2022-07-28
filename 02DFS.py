#Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F',],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.
# It first checks if the current node is unvisited - if yes, it is appended in the visited set.
# Then for each neighbor of the current node, the dfs function is invoked again.
# The base case is invoked when all the nodes are visited. The function then returns.
# Recursive function:
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')
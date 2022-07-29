# Using a Python dictionary to act as an adjacency list
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : [],
}

visitedBFS = []     # List to keep track of visited nodes.
visitedDFS = set()  # Set to keep track of visited nodes.
queue = []          # Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  print("Breadth-First Search:", end=" ")
  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def dfs(visited, graph, node):

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
bfs(visitedBFS, graph, 'A')
print("\nDepth-First Search:", end=" ")
dfs(visitedDFS, graph, 'A')
#DFS Implementation Using Adjacency Matrix
class Graph:
     
    adj = []

    def __init__(self, v, e):
        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)] for j in range(v)]

    def insert_edge(self, start, edge):
        Graph.adj[start][edge] = 1
        Graph.adj[edge][start] = 1

    def DFS(self, start, visited):

        print(start, end = ' ')
        visited[start] = 1
        
        for i in range(self.v):
            if (Graph.adj[start][i] == 1 and (not visited[i])):
                self.DFS(i, visited)

print("Integer-element Graph DFS Using Adjacency Matrix")
v, e = input("Enter no of vertices and edges separated by a space ").split()
g = Graph(int(v), int(e))
g.insert_edge(1, 2)
g.insert_edge(1, 4)
g.insert_edge(2, 3)
g.insert_edge(2, 4)
g.insert_edge(3, 4)
visited = [0] * int(v)
start_node = int(input("Enter source node for DFS "))
g.DFS(start_node, visited)
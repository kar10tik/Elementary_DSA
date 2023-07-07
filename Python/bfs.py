#BFS Implementation Using Adjacency Matrix
class Graph:
	
	adj = []

	def __init__(self, v, e):
		self.v = v
		self.e = e
		Graph.adj = [[0 for i in range(v)] for j in range(v)]

	def insert_edge(self, start, e):
		Graph.adj[start][e] = 1
		Graph.adj[e][start] = 1

	def BFS(self, start):
		visited = [False] * self.v
		q = [start]
		visited[start] = True
		while q:
			vis = q[0]
			print(vis, end = ' ')
			q.pop(0)
			for i in range(self.v):
				if (Graph.adj[vis][i] == 1 and (not visited[i])):
					q.append(i)
					visited[i] = True

print("Integer-element Graph BFS Using Adjacency Matrix")
v, e = input("Enter no of vertices and edges, separated by a space ").split()
g = Graph(int(v), int(e))
g.insert_edge(1, 2)
g.insert_edge(1, 4)
g.insert_edge(2, 3)
g.insert_edge(2, 4)
g.insert_edge(3, 4)
start_node = int(input("Enter source node for BFS "))
g.BFS(start_node)
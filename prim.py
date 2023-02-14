import sys

class Graph():

    adj = []
 
    def __init__(self, vertices):
        self.V = vertices
        Graph.adj = [[0 for i in range(vertices)] for j in range(vertices)]
 
    def displayMST(self, initial): 
        #Initial is the graph to be processed
        print("Edge \tWeight") 
        for i in range(1, self.V):
            print(initial[i], "-", i, "\t", Graph.adj[i][initial[i]])
 
    def min_dist(self, key, MSTset):

        minim = sys.maxsize
        for v in range(self.V):
            if key[v] < minim and MSTset[v] == False:
                minim = key[v]
                min_index = v
        return min_index
 
    def Prim_MST(self):
        
        key = [sys.maxsize] * self.V
        initial = [None] * self.V
        key[0] = 0
        MSTset = [False] * self.V
        initial[0] = -1
 
        for _ in range(self.V):
        # graph[u][v] != 0 for adjacent vertices of m
        # MSTset[v] is False for vertices not yet included in MST
        # Update the key only if graph[u][v] is smaller than key[v]
            u = self.min_dist(key, MSTset)
            MSTset[u] = True
            for v in range(self.V):
                if (Graph.adj[u][v] > 0 and MSTset[v] == False and key[v] > Graph.adj[u][v]):
                        key[v] = Graph.adj[u][v]
                        initial[v] = u
        self.displayMST(initial)

g = Graph(5)
g.graph = [ [0, 5, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0] ]

g.Prim_MST()
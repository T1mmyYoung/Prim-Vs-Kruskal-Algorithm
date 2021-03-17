#Timothy Young, HW8, CS350
##This file contains the UnionFind data structure as well as the 
#implementation for the graph and Kruskal's Algorithm for finding the
#MST
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Amount of vertices(cities/nodes)
        self.graph = [] #Inititalize empty list

    #Add edges by key/string pairing and weight:
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])#City1,city2,weight

    #Recursive Union Find Function
    ##Uses dictionary to replace strings with integer keys
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Unionfind function for union by rank:
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of higher ranking tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #Kruskal's Algorithm:
    def KruskalMST(self):
        result = []  # MST 
        # An index variable, used for sorted edges
        i,e = 0,0
        # Index variable for loop, does not function properly..
        #e = 0
        # Sort all the edges in non-decreasing order
        self.graph = sorted(self.graph,key=lambda item: item[2])
        parent = []
        rank = []
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1 and i<801:
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            #breakpoint()
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            #Else discard the edge
        minimumCost = 0
        print("Edges in the constructed MST")
        #Attempting to invert the dictionary to print the names of the strings for output:
        #inv_dic = {v:k for k, v in cities.items()}
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)
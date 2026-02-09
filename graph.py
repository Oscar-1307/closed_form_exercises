import numpy as np

edges = [(0, 29),
         (0, 46),
         (0, 21),
         (0, 14),
         (0, 38),
         (0, 31),
         (1, 41),
         (1, 31),
         (1, 21),
         (1, 17),
         (2, 9),
         (2, 26),
         (2, 5),
         (2, 25),
         (2, 4),
         (3, 18),
         (3, 30),
         (3, 47),
         (4, 28),
         (4, 9),
         (4, 8),
         (5, 44),
         (5, 12),
         (6, 37),
         (6, 10),
         (7, 23),
         (7, 22),
         (7, 39),
         (9, 19),
         (9, 28),
         (9, 27),
         (11, 33),
         (13, 25),
         (13, 38),
         (13, 29),
         (14, 26),
         (14, 28),
         (14, 39),
         (15, 22),
         (15, 31),
         (15, 19),
         (15, 41),
         (16, 46),
         (16, 26),
         (16, 38),
         (16, 27),
         (17, 40),
         (17, 29),
         (18, 45),
         (18, 42),
         (18, 35),
         (18, 33),
         (18, 47),
         (20, 36),
         (20, 49),
         (20, 42),
         (22, 26),
         (22, 34),
         (23, 31),
         (23, 32),
         (23, 40),
         (24, 31),
         (24, 44),
         (25, 38),
         (26, 31),
         (27, 32),
         (29, 48),
         (29, 41),
         (30, 47),
         (30, 37),
         (33, 36),
         (33, 49),
         (34, 48),
         (35, 45),
         (36, 45),
         (37, 49),
         (37, 45),
         (37, 47),
         (38, 41),
         (40, 48),
         (41, 44),
         (42, 49),
         (43, 48),
         (45, 47)]


# This class represents a directed graph using
# matrix representation

class Graph:

    # Constructor
    def __init__(self):

        # Default array to store graph
        self.graph = np.zeros((0, 0), dtype=bool)

    def reziseArray(self, u):

        # current size
        size_old_graph = self.graph.shape[0]
        # create new (n+1) x (n+1) array filled with False
        new_graph = np.zeros((u, u), dtype=bool)

        # copy old values into the top-left corner
        new_graph[:size_old_graph, :size_old_graph] = self.graph

        self.graph = new_graph

    # Function to add an edge to graph

    def addEdge(self, u, v):

        array_dimension = self.graph.shape[0]
        if (u > v):
            new_size = u + 1
        else:
            new_size = v + 1
        if (new_size > array_dimension):
            self.reziseArray(new_size)
        self.graph[u, v] = True

    def findNode(self, n):
        # True if row i has any True or True if column j has any True
        if np.any(self.graph[i]) or np.any(self.graph[:, j]):
            return True
        return False

    def findEdge(self, u, v):
        return self.graph[u, v]
    # A function used by DFS

    def DFSUtil(self, u, visited):
        visited.add(u)
        print(f"Visiting vertex {u}")

        # check neighbors in matrix row u
        for v in range(self.graph.shape[0]):
            if self.graph[u, v] and not v in visited:
                self.DFSUtil(v, visited)
        return visited

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()

    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        return self.DFSUtil(v, visited)


# Driver's code
if __name__ == "__main__":
    g = Graph()

    for item in edges:
        g.addEdge(item[0], item[1])

    print("Following is Depth First Traversal (starting from vertex 2)")

    # Function call
    print(g.DFS(17))

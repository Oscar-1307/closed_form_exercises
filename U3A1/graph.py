import numpy as np

EDGES = [
    (0, 29), (0, 46), (0, 21), (0, 14), (0, 38), (0, 31),
    (1, 41), (1, 31), (1, 21), (1, 17),
    (2, 9), (2, 26), (2, 5), (2, 25), (2, 4),
    (3, 18), (3, 30), (3, 47),
    (4, 28), (4, 9), (4, 8),
    (5, 44), (5, 12),
    (6, 37), (6, 10),
    (7, 23), (7, 22), (7, 39),
    (9, 19), (9, 28), (9, 27),
    (11, 33),
    (13, 25), (13, 38), (13, 29),
    (14, 26), (14, 28), (14, 39),
    (15, 22), (15, 31), (15, 19), (15, 41),
    (16, 46), (16, 26), (16, 38), (16, 27),
    (17, 40), (17, 29),
    (18, 45), (18, 42), (18, 35), (18, 33), (18, 47),
    (20, 36), (20, 49), (20, 42),
    (22, 26), (22, 34),
    (23, 31), (23, 32), (23, 40),
    (24, 31), (24, 44),
    (25, 38),
    (26, 31),
    (27, 32),
    (29, 48), (29, 41),
    (30, 47), (30, 37),
    (33, 36), (33, 49),
    (34, 48),
    (35, 45),
    (36, 45),
    (37, 49), (37, 45), (37, 47),
    (38, 41),
    (40, 48),
    (41, 44),
    (42, 49),
    (43, 48),
    (45, 47)
]


class Graph:
    """Directed graph using adjacency matrix representation."""

    def __init__(self):
        self.graph = np.zeros((0, 0), dtype=bool)

    def _resize_array(self, size):
        """Resize the adjacency matrix to accommodate new vertices."""
        old_size = self.graph.shape[0]
        new_graph = np.zeros((size, size), dtype=bool)
        new_graph[:old_size, :old_size] = self.graph
        self.graph = new_graph

    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v."""
        new_size = max(u, v) + 1
        if new_size > self.graph.shape[0]:
            self._resize_array(new_size)
        self.graph[u, v] = True

    def find_node(self, n):
        """Check if a node exists in the graph."""
        if n >= self.graph.shape[0]:
            return False
        return np.any(self.graph[n]) or np.any(self.graph[:, n])

    def find_edge(self, u, v):
        """Check if an edge exists from u to v."""
        if u >= self.graph.shape[0] or v >= self.graph.shape[0]:
            return False
        return self.graph[u, v]

    def _dfs_util(self, u, visited):
        """Recursive helper function for DFS traversal."""
        visited.add(u)
        print(f"Visiting vertex {u}")

        for v in range(self.graph.shape[0]):
            if self.graph[u, v] and v not in visited:
                self._dfs_util(v, visited)
        return visited

    def dfs(self, start_vertex):
        """Perform depth-first search starting from the given vertex."""
        visited = set()
        return self._dfs_util(start_vertex, visited)

    def find_connected_graphs(self):
        """Find all connected graphs treating the graph as undirected.

        Returns a tuple of sets, where each set contains nodes in a connected component.
        Example: If nodes {0,1,2} are connected and {3,4} are connected separately,
        returns ({0,1,2}, {3,4})
        """
        visited = set()  # Track which nodes we've already processed
        graphs = []

        # Loop through every node in the graph
        for node in range(self.graph.shape[0]):
            # If node hasn't been visited and exists in the graph
            if node not in visited and self.find_node(node):
                subgraph = set()  # Create new subgraph set
                # Find all nodes connected to this node
                self._explore_graph(node, visited, subgraph)
                graphs.append(subgraph)

        return tuple(graphs)

    def _explore_graph(self, node, visited, subgraph):
        """Recursively explore all nodes reachable from a starting node.

        Treats the directed graph as undirected by checking edges in both directions.
        If A→B exists, we consider A and B connected even though the edge is directional.
        """
        visited.add(node)  # Mark current node as visited
        subgraph.add(node)  # Add node to current subgraph

        # Check all possible neighbors
        for neighbor in range(self.graph.shape[0]):
            if neighbor not in visited:
                # Check if edge exists in either direction (undirected)
                if self.graph[node, neighbor] or self.graph[neighbor, node]:
                    # Recursively explore the neighbor
                    self._explore_graph(neighbor, visited, subgraph)


if __name__ == "__main__":
    g = Graph()

    for u, v in EDGES:
        g.add_edge(u, v)

    print("Connected graphs:")
    graphs = g.find_connected_graphs()
    for i, subgraph in enumerate(graphs, 1):
        print(f"Graph {i}: {sorted(subgraph)}")
    print(f"Total graphs: {len(graphs)}")

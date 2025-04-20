from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # For undirected graph, uncomment the next line:
        # self.graph[v].append(u)

    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        print("DFS traversal starting from node", start)
        visited = set()
        self.dfs_util(start, visited)
        print()

    def bfs(self, start):
        print("BFS traversal starting from node", start)
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print()

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.dfs(2)
g.bfs(2)

class WumpusWorld:
    def __init__(self):
        self.size = 4
        self.agent_pos = (0, 0)
        self.has_gold = False
        self.world = [[[] for _ in range(self.size)] for _ in range(self.size)]
        self.generate_world()

    def generate_world(self):
        # Predefine a simple world with:
        # Gold at (2, 2), Wumpus at (1, 2), Pit at (2, 1)
        self.world[2][2].append('Glitter')
        self.world[1][2].append('Wumpus')
        self.world[2][1].append('Pit')
        self.add_percepts()

    def add_percepts(self):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for i in range(self.size):
            for j in range(self.size):
                if 'Wumpus' in self.world[i][j]:
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < self.size and 0 <= nj < self.size:
                            self.world[ni][nj].append('Stench')
                if 'Pit' in self.world[i][j]:
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < self.size and 0 <= nj < self.size:
                            self.world[ni][nj].append('Breeze')

    def get_percepts(self, pos):
        x, y = pos
        return self.world[x][y]

    def is_safe(self, percepts):
        return 'Stench' not in percepts and 'Breeze' not in percepts

    def explore(self):
        visited = set()
        path = []

        def dfs(pos):
            if pos in visited or not (0 <= pos[0] < self.size and 0 <= pos[1] < self.size):
                return False
            visited.add(pos)
            percepts = self.get_percepts(pos)
            path.append(pos)

            if 'Glitter' in percepts:
                print("Gold found at:", pos)
                self.has_gold = True
                return True

            if not self.is_safe(percepts):
                path.pop()
                return False

            # Try moving in 4 directions
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                next_pos = (pos[0] + dx, pos[1] + dy)
                if dfs(next_pos):
                    return True

            path.pop()
            return False

        if dfs(self.agent_pos):
            print("Safe path to gold:", path)
        else:
            print("No safe path to gold found.")

# Run the Wumpus World agent
world = WumpusWorld()
world.explore()

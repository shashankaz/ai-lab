from collections import deque
import copy

class BlockWorldState:
    def __init__(self, stacks):
        self.stacks = stacks  # List of lists

    def __eq__(self, other):
        return self.stacks == other.stacks

    def __hash__(self):
        return hash(str(self.stacks))

    def __repr__(self):
        return str(self.stacks)

    def is_goal(self, goal):
        return self.stacks == goal.stacks

    def get_possible_moves(self):
        moves = []
        for i, src in enumerate(self.stacks):
            if not src: continue  # Can't move from an empty stack
            block = src[-1]
            for j, dest in enumerate(self.stacks):
                if i == j: continue
                new_stacks = copy.deepcopy(self.stacks)
                new_stacks[i].pop()
                new_stacks[j].append(block)
                moves.append(BlockWorldState(new_stacks))
        return moves

def solve_block_world(start, goal):
    queue = deque()
    visited = set()

    queue.append((start, []))

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        if current.is_goal(goal):
            return path + [current]

        for move in current.get_possible_moves():
            queue.append((move, path + [current]))

    return None


if __name__ == "__main__":
    # Example: 3 blocks A, B, C
    initial_state = BlockWorldState([['C', 'A'], ['B'], []])
    goal_state = BlockWorldState([[], [], ['A', 'B', 'C']])

    solution = solve_block_world(initial_state, goal_state)

    if solution:
        print("Steps to reach the goal:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

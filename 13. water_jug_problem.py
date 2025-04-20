from collections import deque

def is_goal(state, target):
    x, y = state
    return x == target or y == target

def get_next_states(state, A, B):
    x, y = state
    return set([
        (A, y),        # Fill Jug A
        (x, B),        # Fill Jug B
        (0, y),        # Empty Jug A
        (x, 0),        # Empty Jug B
        (max(0, x - (B - y)), min(B, y + x)),  # Pour A -> B
        (min(A, x + y), max(0, y - (A - x)))   # Pour B -> A
    ])

def water_jug_bfs(A, B, target):
    start = (0, 0)
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        if is_goal(current, target):
            return path + [current]

        for next_state in get_next_states(current, A, B):
            queue.append((next_state, path + [current]))

    return None

# Example usage
A = 4  # Jug A capacity
B = 3  # Jug B capacity
target = 2  # Goal

solution = water_jug_bfs(A, B, target)
if solution:
    print("Steps to reach target:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

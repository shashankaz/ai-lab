class State:
    def __init__(self, monkey_pos, box_pos, monkey_on_box, has_banana):
        self.monkey_pos = monkey_pos
        self.box_pos = box_pos
        self.monkey_on_box = monkey_on_box
        self.has_banana = has_banana

    def is_goal(self):
        return self.has_banana

    def __repr__(self):
        return f"(Monkey@{self.monkey_pos}, Box@{self.box_pos}, OnBox={self.monkey_on_box}, HasBanana={self.has_banana})"

    def __eq__(self, other):
        return (self.monkey_pos == other.monkey_pos and
                self.box_pos == other.box_pos and
                self.monkey_on_box == other.monkey_on_box and
                self.has_banana == other.has_banana)

    def __hash__(self):
        return hash((self.monkey_pos, self.box_pos, self.monkey_on_box, self.has_banana))


def get_possible_actions(state):
    actions = []

    positions = ['A', 'B', 'C']

    # Monkey walks to a new position
    for pos in positions:
        if pos != state.monkey_pos and not state.monkey_on_box:
            actions.append(('walk', pos))

    # Monkey pushes box to new position
    for pos in positions:
        if (pos != state.box_pos and
            state.monkey_pos == state.box_pos and
            not state.monkey_on_box):
            actions.append(('push', pos))

    # Monkey climbs box
    if state.monkey_pos == state.box_pos and not state.monkey_on_box:
        actions.append(('climb',))

    # Monkey grasps banana
    if state.monkey_pos == 'B' and state.box_pos == 'B' and state.monkey_on_box:
        actions.append(('grasp',))

    return actions


def apply_action(state, action):
    if action[0] == 'walk':
        return State(action[1], state.box_pos, False, state.has_banana)

    elif action[0] == 'push':
        return State(action[1], action[1], False, state.has_banana)

    elif action[0] == 'climb':
        return State(state.monkey_pos, state.box_pos, True, state.has_banana)

    elif action[0] == 'grasp':
        return State(state.monkey_pos, state.box_pos, state.monkey_on_box, True)

    return state


def monkey_and_banana():
    initial_state = State(monkey_pos='A', box_pos='C', monkey_on_box=False, has_banana=False)
    from collections import deque
    queue = deque()
    queue.append((initial_state, []))
    visited = set()

    while queue:
        current_state, actions = queue.popleft()

        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state.is_goal():
            return actions + [("Goal Reached",)]

        for action in get_possible_actions(current_state):
            next_state = apply_action(current_state, action)
            queue.append((next_state, actions + [action]))

    return None


# Run the planner
plan = monkey_and_banana()
print("Plan to get the banana:")
for step in plan:
    print(step)

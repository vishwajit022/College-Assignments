from collections import deque







# Threw an Error








# Represents the state of the jugs (x, y), where x is the 4-gallon jug and y is the 3-gallon jug
class State:
    def init(self, x, y):
        self.x = x
        self.y = y

    def str(self):
        return f"({self.x}, {self.y})"

    def eq(self, other):
        return self.x == other.x and self.y == other.y

    def hash(self):
        return hash((self.x, self.y))

# Returns a list of successor states from the current state
def get_successors(state):
    successors = []

    # Fill the 4-gallon jug
    successors.append(State(4, state.y))

    # Fill the 3-gallon jug
    successors.append(State(state.x, 3))

    # Empty the 4-gallon jug
    successors.append(State(0, state.y))

    # Empty the 3-gallon jug
    successors.append(State(state.x, 0))

    # Pour from the 4-gallon jug to the 3-gallon jug
    pour_amount = min(state.x, 3 - state.y)
    successors.append(State(state.x - pour_amount, state.y + pour_amount))

    # Pour from the 3-gallon jug to the 4-gallon jug
    pour_amount = min(state.y, 4 - state.x)
    successors.append(State(state.x + pour_amount, state.y - pour_amount))

    return successors

# Breadth-First Search to find a path to the goal state
def breadth_first_search(start_state, goal_state):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        if current_state == goal_state:
            return path

        for successor in get_successors(current_state):
            if successor not in visited:
                new_path = path + [successor]
                queue.append((successor, new_path))

    return None

# Main function
if __name__ == "__main__":
    start_state = State(0, 0)
    goal_state = State(2, 0)

    solution_path = breadth_first_search(start_state, goal_state)

    if solution_path:
        print("Solution Path:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.")

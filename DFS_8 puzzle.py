# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Function to print the puzzle
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Generate all possible moves
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


# Depth Limited DFS
def depth_limited_dfs(state, path, depth_limit):

    # Goal found
    if state == goal:
        return path

    # Depth limit reached
    if len(path) - 1 >= depth_limit:
        return None

    # Explore neighbors
    for neighbor in get_neighbors(state):

        # Avoid going back to a state already in current path
        if neighbor not in path:

            result = depth_limited_dfs(
                neighbor,
                path + [neighbor],
                depth_limit
            )

            if result is not None:
                return result

    return None


# Iterative Deepening DFS
def dfs(start):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        solution = depth_limited_dfs(
            start,
            [start],
            depth
        )

        if solution is not None:
            return solution

        depth += 1


# Starting state
start = (1, 0, 2,
         3, 4, 5,
         6, 7, 8)


# Run DFS
solution = dfs(start)


# Print solution
if solution:

    print("\nSolution found in",
          len(solution) - 1,
          "moves:\n")

    for step in solution:
        print_board(step)

else:
    print("No solution found.")

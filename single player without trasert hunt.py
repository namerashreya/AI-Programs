import random

SIZE = 5

# Random target location
target_row = random.randint(0, SIZE - 1)
target_col = random.randint(0, SIZE - 1)

player_row = 0
player_col = 0

attempts = 0


def calculate_distance(r1, c1, r2, c2):
    # AI heuristic: Manhattan Distance
    return abs(r1 - r2) + abs(c1 - c2)


def display_grid():
    print("\nCurrent Grid:")

    for i in range(SIZE):
        row = ""

        for j in range(SIZE):
            if i == player_row and j == player_col:
                row += " P "
            else:
                row += " . "

        print(row)


print("================================")
print("       AI GRID NAVIGATION")
print("================================")
print("Reach the hidden target!")
print()
print("Commands:")
print("U = Up")
print("D = Down")
print("L = Left")
print("R = Right")
print("Q = Quit")


while True:

    display_grid()

    # Calculate AI distance
    distance = calculate_distance(
        player_row,
        player_col,
        target_row,
        target_col
    )

    print("AI Distance:", distance)

    # Check if target reached
    if player_row == target_row and player_col == target_col:
        print("\nCongratulations!")
        print("You reached the target!")
        print("Attempts:", attempts)
        break

    move = input("\nEnter your move: ").upper()

    if move == "Q":
        print("Game Over!")
        break

    attempts += 1

    new_row = player_row
    new_col = player_col

    # Movement
    if move == "U":
        new_row -= 1

    elif move == "D":
        new_row += 1

    elif move == "L":
        new_col -= 1

    elif move == "R":
        new_col += 1

    else:
        print("Invalid move!")
        attempts -= 1
        continue

    # Check boundaries
    if 0 <= new_row < SIZE and 0 <= new_col < SIZE:
        player_row = new_row
        player_col = new_col
    else:
        print("You cannot move outside the grid!")
        attempts -= 1


print("\nThank you for playing!")

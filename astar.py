import heapq

maze = [
    list("###############"),
    list("#P     #     G#"),
    list("# ###     ### #"),
    list("#             #"),
    list("###############")
]

ROWS = len(maze)
COLS = len(maze[0])


def printMaze():
    for row in maze:
        print("".join(row))


def find(ch):
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == ch:
                return (i, j)


def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def getNeighbors(node):
    r, c = node

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    ans = []

    for dr, dc in moves:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if maze[nr][nc] != '#':
                ans.append((nr, nc))

    return ans


def clearStars():
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == '*':
                maze[i][j] = ' '


def hint():
    start = find('P')
    goal = find('G')

    clearStars()

    print("\nCurrent Position :", start)
    print("\nPossible Moves")
    print("-----------------------------------")
    print("Direction\tg\th\tf")

    bestF = 100000
    bestNode = None

    for nxt in getNeighbors(start):
        g = 1
        h = heuristic(nxt, goal)
        f = g + h

        direction = ""

        if nxt[0] == start[0] - 1:
            direction = "Up"
        elif nxt[0] == start[0] + 1:
            direction = "Down"
        elif nxt[1] == start[1] - 1:
            direction = "Left"
        elif nxt[1] == start[1] + 1:
            direction = "Right"

        print(direction, "\t\t", g, "\t", h, "\t", f)

        if f < bestF:
            bestF = f
            bestNode = nxt

    if bestNode:
        r, c = bestNode

        if maze[r][c] == ' ':
            maze[r][c] = '*'

        print("\nBest Move :", bestNode)
        print("Minimum f =", bestF)

    input("\nPress Enter...")


while True:

    printMaze()

    print("\nControls")
    print("W = Up")
    print("S = Down")
    print("A = Left")
    print("D = Right")
    print("H = Hint")
    print("Q = Quit")

    move = input("\nEnter Choice : ").lower()

    if move == 'q':
        break

    if move == 'h':
        hint()
        continue

    clearStars()

    r, c = find('P')

    nr = r
    nc = c

    if move == 'w':
        nr -= 1
    elif move == 's':
        nr += 1
    elif move == 'a':
        nc -= 1
    elif move == 'd':
        nc += 1
    else:
        continue

    if maze[nr][nc] == '#':
        continue

    if maze[nr][nc] == 'G':

        maze[r][c] = ' '
        maze[nr][nc] = 'P'

        printMaze()

        print("\nCongratulations!")
        print("You reached the Goal.")

        break

    maze[r][c] = ' '
    maze[nr][nc] = 'P'
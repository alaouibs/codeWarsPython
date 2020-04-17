def path_finder(maze):
    maze = a.split('\n')
    unvisited = set()
    visited = set()
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == '.':
                unvisited.add((i, j))
            maze[i] = [c for c in maze[i]]
    start = (0, 0)
    end = (len(maze ) - 1, len(maze) - 1)
    current = start
    dijisktraMatrix = {}
    for pos in unvisited:
        dijisktraMatrix[pos] = [9999, None]

    dijisktraMatrix[(0, 0)][0] = 0
    neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while len(unvisited) > 0:
        current = 
    print(dijisktraMatrix)
    print(maze)
    print(unvisited)
    return

a = "\n".join([
  ".W.",
  ".W.",
  "..."
])


print(path_finder(a))
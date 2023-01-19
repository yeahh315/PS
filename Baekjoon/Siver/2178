import sys

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
maze.insert(0, [0 for _ in range(m)])
maze.append([0 for _ in range(m)])
for i in range(len(maze)):
    tmp = maze[i]
    tmp.insert(0,0)
    tmp.append(0)
    maze[i] = tmp

visited = [[0 for _ in range(m + 2)] for _ in range(n +2)]

def find_root(arrived_x, arrived_y):
    root = []
    now_x, now_y = 1, 1
    root.append([(now_x, now_y)])
    visited[now_x][now_y] = 1
    index = 0
    while True:
        tmp = []
        for (i, j) in root[index]:
            if maze[i + 1][j] == 1 and visited[i + 1][j] !=1:
                tmp.append((i+1, j))
                visited[i+1][j] = 1
            if maze[i - 1][j] == 1 and visited[i - 1][j] !=1:
                tmp.append((i-1, j))
                visited[i - 1][j] = 1
            if maze[i][j+1] == 1 and visited[i][j+1] !=1:
                tmp.append((i, j+1))
                visited[i][j + 1] = 1
            if maze[i][j-1] == 1 and visited[i][j -1] !=1:
                tmp.append((i, j-1))
                visited[i][j - 1] = 1
        root.append(tmp)
        if (arrived_x, arrived_y) in root[-1]:
            break
        index += 1

    return len(root)

print(find_root(n, m))

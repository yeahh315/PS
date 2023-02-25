import sys

n, m = map(int, sys.stdin.readline().split())
num_paper = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (-1, 1), (1, 1), (0, 2)]
move_ = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_rest(selected, search):
    maximum = 0
    for i, j in search:
        now = num_paper[i][j]
        for k, l in move_:
            if 0 <= i + k < n and 0 <= j + l < m and (i + k, j + l) not in selected:
                maximum = max(maximum, now + num_paper[i + k][j + l])
    return maximum

def tetromino():
    maximum = 0
    for i in range(n):
        for j in range(0, m - 1):
            selected = [(i, j), (i, j + 1)]
            now = num_paper[i][j] + num_paper[i][j + 1]
            tmp_max, searching = [], []
            for x, y in move:
                x += i
                y += j
                if 0 <= x < n and 0 <= y < m: 
                    searching.append((x, y))
                    tmp_max.append(num_paper[x][y])
            tmp_max.sort()
            maximum = max(maximum, find_rest(selected, searching) + now)
            maximum = max(maximum, now + tmp_max[-2] + tmp_max[-1])
    for i in range(m):
        for j in range(0, n - 3):
            length = num_paper[j][i] + num_paper[j + 1][i] + num_paper[j + 2][i] + num_paper[j + 3][i]
            maximum = max(maximum, length) 

    return maximum

print(tetromino())

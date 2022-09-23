import sys
from collections import deque
sys.setrecursionlimit(10**6)

que = deque()
def find(i, j):
    if farm[i][j] == 1:
        if (i, j) not in que:
            que.append((i, j))
        check = 0
        # 좌
        if j - 1 >= 0 and (i, j - 1) not in que:
                find(i, j - 1)
                check += farm[i][j-1]
        # 상
        if i - 1 >= 0 and (i - 1, j) not in que:
                find(i - 1, j)
                check += farm[i-1][j]
        # 우
        if j + 1 < len(farm[0]) and (i, j + 1) not in que:
                find(i, j + 1)
                check += farm[i][j + 1]
        # 하
        if i + 1 < len(farm) and (i + 1, j) not in que:
                find(i + 1, j)
                check += farm[i + 1][j]

        if check == 0:
            x, y = que.pop()
            farm[x][y] = 0
            if len(que) == 0: return 1
            x, y = que[-1]

    else:
        return 0

# 테스트 케이스 개수 T, 가로 세로 M N, 배추 개수 K
T = int(sys.stdin.readline())
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = [[0 for j in range(M)] for k in range(N)]
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        farm[y][x] = 1
    worm = 0
    for i in range(len(farm)):
        for j in range(len(farm[0])):
            worm += find(i,j)
    print(worm)

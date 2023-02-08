import sys

m, n, h = map(int, sys.stdin.readline().split())

# 3차원 박스 안의 토마토 상태를 저장하기 위한 Dict
box = {(i, j, k) : 0 for i in range(h) for j in range(n) for k in range(m)}
state = {1:[], -1:[], 0:[]}   # 상태 별 토마토의 좌표 저장

for i in range(h):
    tmp = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    for j in range(len(tmp)):
        for k in range(len(tmp[j])):
            box[(i, j, k)] = tmp[j][k]
            state[tmp[j][k]].append((i, j, k))

tmp_reap = [] # 한 번 탐색 시 바로 상태를 업데이트 해주면 안되기 때문에 임시로 익은 토마토를 저장
def reap(i, j, k):  # 익은 토마토와 인접한 토마토가 안익었다면 익도록
    if box[(i, j, k)] == 0:
        box[(i, j, k)] = 1
        tmp_reap.append((i, j, k))

day = -1
while state[1]: # 탐색하지 않은 익은 토마토가 없을 때까지 지속
    day += 1
    for i, j, k in state[1]:
        #위, 아래, 상, 하, 좌, 우 
        if i > 0: reap(i - 1, j, k)
        if i < h - 1: reap(i + 1, j, k)
        if j > 0: reap(i, j - 1, k)
        if j < n - 1: reap(i, j + 1, k)
        if k > 0: reap(i, j, k - 1)
        if k < m - 1: reap(i, j, k + 1)
    state[1].clear()  # 탐색한 익은 토마토는 다시 탐색하지 않음
    state[1] = tmp_reap.copy()  # 새로 탐색할 익은 토마토를 넣어줌
    tmp_reap.clear()

if list(box.values()).count(0) != 0: print(-1)  # 탐색이 끝난 후 안익은 토마토가 있다면 -1
else: print(day)

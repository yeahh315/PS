import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 'normal'과 'weakness' 키를 이용해 각각 visited를 만들어줌
visited = {'normal' : [[0 for _ in range(n)]for _ in range(n)], 'weakness': [[0 for _ in range(n)]for _ in range(n)]}
# 'normal'과 'weakness' 키를 이용해 각 색이 같게 보이면 색 key값에 따른 value를 동일하게 설정
state = {'normal' : {'R' : 0, 'G' : 1, 'B' : 2}, 'weakness' :{'R' : 0, 'G' : 0, 'B' : 2}}

def area(states, color, i, j):  # state에는 'normal' 혹은 'weakness'가 들어감
    visited[states][i][j] = 1
    if i > 0: 
        if visited[states][i-1][j] == 0 and state[states][grid[i-1][j]] == state[states][color]: area(states, color, i-1, j)
    if i < n - 1: 
        if visited[states][i+1][j] == 0 and state[states][grid[i+1][j]] == state[states][color]: area(states, color, i+1, j)
    if j > 0: 
        if visited[states][i][j-1] == 0 and state[states][grid[i][j-1]] == state[states][color]: area(states, color, i, j - 1)
    if j < n - 1: 
        if visited[states][i][j + 1] == 0 and state[states][grid[i][j + 1]] == state[states][color]: area(states, color, i, j + 1)
    return 1

cnt_normal, cnt_weakness = 0, 0
for i in range(n):
    for j in range(n):
        if visited['normal'][i][j]: continue  # 방문했으면 탐색하지 않고 넘어감
        else: cnt_normal += area('normal', grid[i][j], i, j)  # 방문하지 않은 노드에 대해 탐색

        if visited['weakness'][i][j]: continue
        else: cnt_weakness += area('weakness', grid[i][j], i, j)
            
print(cnt_normal, cnt_weakness)

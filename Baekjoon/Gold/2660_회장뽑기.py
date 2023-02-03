# Floyd Warshall 

import sys
inf = 50

n = int(sys.stdin.readline())
friends = [[50 for _ in range(n + 1)] for _ in range(n + 1)]

# graph 생성
while True:
    a, b = map(int, sys.stdin.readline().split())
    if (a, b) == (-1, -1): break
    friends[a][b], friends[b][a] = 1, 1

min_f = [1 for _ in range(n + 1)]
min_f[0] = inf

def floyd_warshall(middle):
    for i in range(1, n + 1):
        friends[i][i] = 0
        if i == middle: continue
        for j in range(i, n + 1):
            if j == middle: continue
            friends[i][j] = min(friends[i][j], friends[i][middle] + friends[middle][j])
            friends[j][i] = friends[i][j]
            
        min_f[i] = max(friends[i][1:])

for i in range(n):
    floyd_warshall(i + 1)

min_friends = min(min_f)
cnt_m = []
for i in range(1, len(min_f)):
    if min_f[i] == min_friends: 
        cnt_m.append(i)
    
print(min_friends, len(cnt_m))
print(*cnt_m)

# Bellman-Ford

import sys

inf = 500 * 100000

# input
n, m = map(int, sys.stdin.readline().split())
graph = [{} for _ in range(n + 1)]
bus = []  # bus[ind][0]:start [1]:end [2]:cost 
distance = [inf for _ in range(n + 1)]  # init distance

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    if graph[start].get(end) == None: graph[start][end] = cost
    else: graph[start][end] = min(graph[start][end], cost)
    bus.append([start, end, graph[start][end]])

def min_cost(start):
    distance[start] = 0
    for _ in range(n):  # O(m*n)
        not_update = distance.copy()
        for j in range(len(bus)):
            s, e, c = bus[j]
            if (distance[e] > distance[s] + c) and (distance[s] != inf): distance[e] = distance[s] + c
            if distance[start] < 0: return 1
    if not_update != distance: return 1   # m*n 이후에도 계속 distance 값이 업데이트되면 음수 간선이 있는 것으로 간주
    return 0

check = min_cost(1)
if check: print(-1)
else:
    for i in range(2, len(distance)):
        if distance[i] == inf: print(-1)
        else: print(distance[i])

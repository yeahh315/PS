# Dijkstra 

import sys, heapq
max_distance = 987654321

# input
city, bus_num = int(sys.stdin.readline()), int(sys.stdin.readline())
bus_info = [{} for _ in range(city + 1)]
visit = {}  # 방문 시 city : 1
distance = {i : max_distance for i in range(1, city + 1)}

# init 비용
for _ in range(bus_num):
    start, end, cost = map(int, sys.stdin.readline().split())
    if bus_info[start].get(end) == None: bus_info[start][end] = cost
    else: bus_info[start][end] = min(bus_info[start][end], cost)

start, end = map(int, sys.stdin.readline().split())
distance[start] = 0

heap = []
heapq.heappush(heap, (0, start))

while heap:
    x, now = heapq.heappop(heap)
    visit[now] = 1
    if visit.get(end) != None: break    

    for i in list(bus_info[now].keys()):
        if visit.get(i): continue
        if distance[i] > distance[now] + bus_info[now][i]:
            distance[i] = distance[now] + bus_info[now][i]
            if visit.get(i) == None:
                heapq.heappush(heap, (distance[i], i))
    
print(distance[end])

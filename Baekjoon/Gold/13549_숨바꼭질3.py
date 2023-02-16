from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
inf = 10**10
distance = {i : inf for i in range(100000 * 2 + 1)}
visit = [0 for i in range(100000 * 2 + 1)]

def hide_and_seek(a, b):
    distance[a] = 0
    q = deque()
    q.append(a)

    while q:
        now = q.popleft()
        visit[now] = 1
        if now == b: break  # 동생을 찾으면 종료

        if distance.get(now * 2) != None: 
            if visit[now * 2] == 0 and distance[now] <= distance[now * 2]: # 현재 노드에서 순간이동 한 시간이 더 짧다면
                distance[now * 2] = distance[now]
                q.appendleft(now * 2) # 가중치가 0이므로 우선 탐색하기 위해 왼쪽에 append
        if distance.get(now + 1) != None: 
            if visit[now + 1] == 0 and distance[now] + 1 <= distance[now + 1]:
                distance[now + 1] = distance[now] + 1
                q.append(now + 1)
        if distance.get(now - 1) != None: 
            if visit[now - 1] == 0 and distance[now] + 1 <= distance[now - 1]:
                distance[now - 1] = distance[now] + 1
                q.append(now - 1)

    print(distance[b])

hide_and_seek(n, k)


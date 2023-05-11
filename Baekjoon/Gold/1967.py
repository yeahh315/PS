import sys
from collections import deque

node_cnt = int(sys.stdin.readline())
graph_ = {i : [] for i in range(0, node_cnt + 1)}

# make graph
for _ in range(node_cnt - 1):
    parent, child, cost = map(int, sys.stdin.readline().split())
    graph_[parent].append((child, cost))
    graph_[child].append((parent, cost))

def find_node_and_cost(start_node):
    visit = [0 for _ in range(node_cnt + 1)]
    visit[start_node] = 1
    queue = deque()
    queue.append((start_node, 0))
    tmp_node, tmp_cost = 0, 0

    while queue:
        now_node, now_cost = queue.popleft()
        check = 0 
        for next_node, next_cost in graph_[now_node]:
            new_cost = now_cost + next_cost
            if visit[next_node] == 0:
                check = 1
                visit[next_node] = 1
                queue.append((next_node, new_cost))
        if check == 0:
            if tmp_cost < now_cost:
                tmp_node, tmp_cost = now_node, now_cost
    return tmp_node, tmp_cost

once_node, once_cost = find_node_and_cost(1)
second_node, second_cost = find_node_and_cost(once_node)
print(second_cost)

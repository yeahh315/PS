import sys
SIZE = 100000

n, k = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(SIZE * 2)]
root = []
def cal_time(x, y):
    if x == y:
        return
    root.append([x])
    visited[x] = 1
    index = 0

    while True:
        tmp = []
        for i in root[index]:
            if i - 1 == y or i + 1 == y or i * 2 == y:
                return
            if i > 0 and visited[i - 1] != 1:
                visited[i-1] = 1
                tmp.append(i - 1)
            if i < 100000 and visited[i + 1] != 1:
                visited[i + 1] = 1
                tmp.append(i + 1)
            if i != 0 and i <= 50000 and visited[i * 2] != 1:
                visited[i * 2] = 1
                tmp.append(2*i)
        root.append(tmp)
        index += 1


cal_time(n, k)
print(len(root))

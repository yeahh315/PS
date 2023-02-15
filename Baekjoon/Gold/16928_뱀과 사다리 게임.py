import sys

n, m = map(int, sys.stdin.readline().split())
gameMap = {i : set([i + j for j in range(1, 7)]) for i in range(1, 101)}  # key값에서 주사위를 굴려 이동할 수 있는 칸을 value에 저장
ladder_snake = {}   # 뱀과 사다리 정보 저장
visited = [0 for i in range(101)]   # 아직 방문하지 않았으면 0

for i in range(n+m):
    start, end = map(int, sys.stdin.readline().split())
    ladder_snake[start] = end

def bfs(start):
    count_dice = 0  # 주사위 굴린 횟수 저장
    queue = [[start]]
    visited[start] = 1

    check_arrived = 0 
    while queue:
        count_dice += 1
        tmp_queue = []  # 한번의 턴에 갈 수 있는 모든 칸 저장
        now = queue.pop(0) 
        for i in now:
            for j in gameMap[i]:
                if j == 100:
                    check_arrived = 1
                    break
                if ladder_snake.get(j) != None: j = ladder_snake[j]   # 그 칸에 뱀이나 사다리가 있으면 즉시 이동
                if visited[j] == 0: 
                    tmp_queue.append(j)
                    visited[j] = 1
        if check_arrived: break
        queue.append(tmp_queue)
    
    return count_dice

print(bfs(1))

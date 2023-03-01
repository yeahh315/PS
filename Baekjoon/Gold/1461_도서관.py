import sys
from heapq import heappush, heappop

n, m = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))
step = 0

negative, positive = [], [] # 어차피 양수와 음수를 따로 이동해야 하므로 따로 heap으로 저장

for i in books:
    if i > 0: heappush(positive, -i)
    else: heappush(negative, i)

max_, min_ = 0, 0
if positive: max_ = positive[0]
if negative: min_ = negative[0]

while positive:
    for i in range(m): # 책을 한번에 들 수 있는 수 만큼 반복
        if len(positive) == 0: break
        if i == 0: step += -heappop(positive) # 가장 무거운 책을 들러 가는 동안 
        else: heappop(positive) # 들 수 있는 책의 최대 개수만큼 가져옴
while negative:
    for i in range(m):
        if len(negative) == 0: break
        if i == 0: step += -heappop(negative)
        else: heappop(negative)

step *= 2 # 왕복이므로 * 2
step -= -min(max_, min_) # 가장 멀리있는 책은 마지막에 들기 때문에 편도 

print(step)

import sys
from heapq import heappush, heappop

# 중간 값들은 항상 heap[0]에 존재
heap = [] # 새로 들어오는 수를 저장할 minHeap
middle_num = [] # 중간 값보다 작은 수를 저장할 maxHeap
def middle(num, ind):
    heappush(heap, num)
    if ind > len(middle_num): # 중간 값보다 작은 값들을 heap에서 pop해 middle_num에 넣어줌
        tmp = heappop(heap)
        heappush(middle_num, (-tmp, tmp))
    if len(middle_num): 
        if heap[0] < middle_num[0][1]: # 만약 새로 들어온 값이 중간 값보다 작으면 바꿔줌
            tmp = heappop(heap)
            heappush(middle_num, (-tmp, tmp))
            heappush(heap, heappop(middle_num)[1])

    print(heap[0])

n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    middle(num, i//2) # 들어온 수와 중간 값의 index

import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

card = {}

for i in list(set(arr)):
    card[i] = 0
for i in arr:
    card[i] += 1

for i in num:
    if card.get(i) != None:
        print(card[i], end=' ')
    else:
        print(0, end=' ')

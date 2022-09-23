import sys, math
N, want = map(int, sys.stdin.readline().split())
length = list(map(int, sys.stdin.readline().split()))

if sum(length) - min(length) * len(length) <= want:
    print((sum(length) - want) // len(length))

else:
    length.sort()
    min = 0
    max = len(length) - 1
    while max - min != 1:
        mid = (min + max) // 2
        if sum(length[mid + 1:]) - len(length[mid + 1:]) * length[mid] < want:
            max = mid
        else:
            min = mid
    length = length[max:]
    print((sum(length) - want) // len(length))

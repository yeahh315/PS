import math, sys
def cal_min(n):
    if count[n] > 0:
        return count[n]
    if math.floor(n ** (1/2)) ** 2 == n:
        count[n] = 1
        return count[n]
    else:
        max_root = math.floor(n ** (1/2))
        min_value = cal_min(max_root ** 2) + cal_min(n - max_root ** 2)
        while max_root ** 2 + (max_root + 1) ** 2 >= n:
            min_value = min(min_value, cal_min(max_root ** 2) + cal_min(n - max_root ** 2))
            max_root -= 1
        count[n] = min_value
        return count[n]

N = int(sys.stdin.readline())
count = [0] * (N + 1)
print(cal_min(N))

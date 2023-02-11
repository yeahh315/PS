import sys
n, k = map(int, sys.stdin.readline().split())
save = {(i, j) : 0 for i in range(n + 1) for j in range(k + 1)} # i까지의 수 j자리로 i를 만들 수 있는 개수

def dp(a, b):
    if save[(a, b)] > 0: return save[(a, b)]

    if b <= 1 or a == 0:
        save[(a, b)] = 1
        return save[(a, b)]

    for i in range(a + 1):
        save[(a, b)] += dp(i, b - 1)
    
    return save[(a, b)]

print(dp(n, k) % 1000000000)

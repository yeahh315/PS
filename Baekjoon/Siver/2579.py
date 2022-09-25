import sys
N = int(sys.stdin.readline())

stair = [0] * (N + 1)
dp = [0] * (N + 1)
for i in range(1, N + 1):
    stair[i] = int(sys.stdin.readline())
    dp[i] = max(dp[i - 3] + stair[i - 1], dp[i - 2]) + stair[i]

print(dp[N])

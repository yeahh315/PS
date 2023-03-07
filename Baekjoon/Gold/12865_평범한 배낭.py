import sys
n, k = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(k + 1)]]  # 배낭에 아무것도 담지 않았을 때 초기화

for i in range(1, n + 1):
    weight, value = map(int, sys.stdin.readline().split())
    dp.append(dp[i - 1].copy())   # 이전 물건까지 담았을 때 가치의 최댓값
    for j in range(weight, k + 1):
        new_weight = value + dp[i - 1][j - weight]  
        if new_weight > dp[i][j]: dp[i][j] = new_weight # 새로운 물건을 담았을 때 가치가 더 크면 업데이트

print(dp[n][k])

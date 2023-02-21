# 여집합을 이용한 풀이
import math, sys
full_time, section_time, section = 90, 5, 90 // 5

# 소수 판별 함수
def is_prime_number(x):
    if x < 2: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True
# team 매개변수가 i개의 골을 넣을 확률 (i가 소수가 아닐 때의 확률을 구하는 것이므로 i가 소수이면 0)
def cal_prob(team, i):
    if is_prime_number(i): return 0 
    else: return math.comb(section, i) * (prob[team] ** i) * ((1 - prob[team]) ** (section - i))
# DP를 이용해 값 누적
def DP(team):
    dp[team][0] = cal_prob(team, 0)
    for i in range(1, section + 1):
        dp[team][i] = dp[team][i - 1] + cal_prob(team, i)
    return dp[team][section]

A, B = int(sys.stdin.readline()), int(sys.stdin.readline())
prob = {'A' : A * 0.01, 'B' : B * 0.01}
dp = {'A' : [0 for _ in range(section + 1)], 'B' : [0 for _ in range(section + 1)]}

print(1 - DP('A') * DP('B'))

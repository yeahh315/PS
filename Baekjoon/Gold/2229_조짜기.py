import sys
n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
team = [0 for _ in range(n)]

def DP(end):
    if end == 0: return 0

    ind = 0 # ind 까지의 학생은 조 확정
    for i in range(0, end):
        maximum = max(score[ind:i+1]) - min(score[ind:i+1])
        for j in range(ind, i):
            compare = team[j] + max(score[j+1:i+1]) - min(score[j+1:i+1])
            if maximum < compare:
                maximum = compare
                ind = j
        team[i] = maximum
    
    return team[end-1]

print(DP(n))

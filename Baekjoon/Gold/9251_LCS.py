import sys
A, B = list(sys.stdin.readline().strip()), list(sys.stdin.readline().strip())
LCS = [[0 for _ in range(len(A) + 1)]for _ in range(len(B) + 1)]

LCS_length = 0
for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]: LCS[i][j] = LCS[i - 1][j - 1] + 1
        else: LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

        if LCS[i][j] > LCS_length: LCS_length = LCS[i][j]

print(LCS_length)

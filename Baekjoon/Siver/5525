import sys

n, s, = int(sys.stdin.readline()), int(sys.stdin.readline())
string = sys.stdin.readline().strip()

Pn = 'IO' * n + 'I'

cnt, i, ioi = 0, 0, 0

while i < s:
    if string[i : i + 3] == "IOI":
        ioi += 1
        if ioi == n:
            cnt += 1
            ioi -= 1
        i += 2
    else:
        i += 1
        ioi = 0
print(cnt)

import sys

seq = []
ans = []
s_tack = []
num, top = 1, 0
n = int(sys.stdin.readline())
for i in range(n):
    seq.append(int(sys.stdin.readline()))
check = True

for i in seq:
    while num <= i:
        s_tack.append(num)
        ans.append('+')
        num += 1
    top = s_tack[-1]
    if top == i:
        s_tack.pop()
        ans.append('-')
    else:
        check = False
        break
if check:
    print('\n'.join(ans))
else:
    print("NO")

import sys

N, r, c = map(int, sys.stdin.readline().split())

visit = 0
ind = N - 1
while not (r == 0 and c == 0):
    if r // (2 ** ind) == 0 and c // (2 ** ind) == 0:
        visit += 0 * ((2 ** ind) ** 2)
    elif r // (2 ** ind) == 0 and c // (2 ** ind) == 1:
        visit += 1 * ((2 ** ind) ** 2)
    elif r // (2 ** ind) == 1 and c // (2 ** ind) == 0:
        visit += 2 * ((2 ** ind) ** 2)
    elif r // (2 ** ind) == 1 and c // (2 ** ind) == 1:
        visit += 3 * ((2 ** ind) ** 2)
    r %= (2 ** ind)
    c %= (2 ** ind)
    ind -= 1

print(visit)

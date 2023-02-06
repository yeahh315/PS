import sys

n, p, q, x, y = map(int, sys.stdin.readline().split())

def seq(stop):
    if a.get(stop) == None: a[stop] = 0
    if a[stop] > 0: return a[stop]

    if stop <= 0: 
        a[stop] = 1
        return a[stop]
    else:
        a[stop] = seq((stop//p) - x) + seq((stop//q) - y)

    return a[stop]

a = {}
print(seq(n))

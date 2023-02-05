# DP, 메모리 초과는 딕셔너리로

import sys
n, p, q = map(int, sys.stdin.readline().split())

def seq(stop):
    if a.get(stop) == None: a[stop] = 0
    if a[stop] > 0: return a[stop]

    if stop == 0: a[stop] = 1
    else: a[stop] = seq(stop//p) + seq(stop//q)

    return a[stop]

a = {}
print(seq(n))

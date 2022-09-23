import sys
import math

def cal_num_of_line(line_arr, cut):  #랜선 배열, 자를 길이
    answer = 0
    for i in range(len(line_arr)):
        answer += line_arr[i] // cut
    return answer

k, n = map(int, sys.stdin.readline().split())
line = []
for i in range(k):
    line.append(int(sys.stdin.readline()))

#최대, 최소 랜선의 길이
max_line = sum(line) // n + 1
min_line = min(line) // int(math.ceil(n / k))

while(max_line - min_line != 1):
    tmp = cal_num_of_line(line, (max_line + min_line) // 2)
    if tmp >= n:
        min_line = (max_line + min_line) // 2
    else:
        max_line = (max_line + min_line) // 2

print(min_line)

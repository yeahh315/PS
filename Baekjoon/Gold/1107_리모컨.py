import sys

# input
want_num, cnt_button = int(sys.stdin.readline()), int(sys.stdin.readline())
if cnt_button != 0: bust_button = list(sys.stdin.readline().split())
else: bust_button = []

button = {str(i) : 1 for i in range(10)}
for i in bust_button: button[i] = 0   # 버튼이 고장나면 value값 = 0, 고장나지 않으면 value값 = 1
    
def press_num(stop):
    start_p, start_n = str(want_num), str(want_num)
    
    while True:   # 주어진 숫자보다 큰 수 중 만들 수 있는 가장 작은 수
        check_p = 0   # 고장난 버튼이 있는지 판별
        for i in start_p:
            if button[i] == 0: 
                check_p = 1   # 고장난 버튼이 존재하면 1
                break
        if check_p:   # 고장난 버튼 존재 시 +1
            start_p = str(int(start_p) + 1)
            if int(start_p) >= want_num + stop: break   # 큰 수의 max
        else: break
          
    while True:   # 주어진 숫자보다 작은 수 중 만들 수 있는 가장 큰 수
        check_n = 0
        for i in start_n:
            if button[i] == 0: 
                check_n = 1
                break
        if check_n: 
            start_n = str(int(start_n) - 1)
            if int(start_n) <= want_num - stop: break
            if int(start_n) < 0: 
                start_n = "-1000000"
                break
        else: break
    
    # 눌러야 하는 버튼 갯수 계산
    plus = int(start_p) - want_num + len(start_p)
    minus = want_num - int(start_n) + len(start_n)
    return min(plus, minus, stop)
    


if want_num == 100: print(0)
else:
    if want_num > 100: plus_minus = want_num - 100
    else: plus_minus = 100 - want_num
    print(press_num(plus_minus))

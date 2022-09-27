def solution(N, stages):
    answer = []
    fail = [0] * N
    user = len(stages)
    
    for i in stages:
        if i <= N:
            fail[i - 1] += 1
    for i in range(len(fail)):
        if user == 0:
            fail[i] =0
        else:
            tmp = fail[i]
            fail[i] = fail[i] / user
            user -= tmp
        
        
    for i in range(len(fail)):
        answer.append(fail.index(max(fail)) + 1)
        fail[fail.index(max(fail))] = -1
        
    return answer

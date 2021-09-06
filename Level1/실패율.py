def solution(N, stages):
    clear_cnt = [0 for n in range(N+2)]
    for i in range(len(stages)):
        clear_cnt[stages[i] - 1] += 1
        
    failure = [0 for n in range(N)]
    sub_sum = 0
    for i in range(N, 0, -1):
        sub_sum += clear_cnt[i]
        failure[i-1] = 0 if clear_cnt[i-1] == 0 else clear_cnt[i-1] / (sub_sum + clear_cnt[i-1])
        
    answer = []
    f = sorted(failure, reverse = True)
    for i in range(N):
        answer.append(failure.index(f[i]) + 1)
        failure[failure.index(f[i])] = 2
    return answer

import math
def solution(progresses, speeds):
    answer = []
    cur = 0
    while cur < len(progresses):
        days = math.ceil((100 - progresses[cur]) / speeds[cur])
        done = 0
        flag = True
        for i in range(cur, len(progresses)):
            progresses[i] += days * speeds[i]
            if flag: #같이 배포 가능
                if progresses[i] >= 100:
                    done += 1
                else:
                    flag = False
        answer.append(done)
        cur += done
    return answer

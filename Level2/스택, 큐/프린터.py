def solution(priorities, location):
    cnt = 0
    while len(priorities) > 1:
        cur = priorities.pop(0)
        if cur >= max(priorities): #현재 문서의 우선순위가 가장 높을 때
            if location == 0: #내가 요청한거면
                return cnt + 1
            else:
                location -= 1
            cnt += 1
        else: #현재 문서보다 높은 우선순위의 문서가 있을 때
            if location == 0: #내가 요청한거면
                location = len(priorities)
            else:
                location -= 1
            priorities.append(cur)
    return cnt + 1

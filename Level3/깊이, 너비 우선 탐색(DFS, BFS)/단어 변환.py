def solution(begin, target, words):
    if target not in words:
        return 0
    visited=[begin] #탐색한 단어 저장
    queue=[[begin,0]] #탐색할 단어와 현재 단계 저장
    while queue:
        cur=queue.pop(0)
        if cur[0]==target: #target을 완성하면 리턴
            return cur[1]
        for w in set(words)-set(visited):
            if w in visited: #탐색하지 않은 단어
                continue
            diff=0
            for j in range(len(begin)):
                if cur[0][j]!=w[j]:
                    diff+=1
            if diff==1: #차이가 1이면
                queue.append([w,cur[1]+1])
                visited.append(w)

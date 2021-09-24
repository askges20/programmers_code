def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    for i in range(len(word)):
        cur = word[i]
        tmp = 0
        for j in range(5 - i):
            tmp += 5 ** j
        answer += tmp * alpha.index(cur) + 1
    return answer

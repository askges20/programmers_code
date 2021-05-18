def solution(brown, yellow):
    m = 1
    while(True):
        n = (brown + 4)/2 - m
        cal = (m - 2) * (n - 2)
        if cal == yellow:
            answer = [max(m,n), min(m,n)]
            return answer
        m = m + 1
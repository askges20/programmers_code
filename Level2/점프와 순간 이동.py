def solution(n):
    cur = n
    ans = 0
    while True:
        if cur == 0:
            break
        if cur % 2 == 0: #짝수
            cur /= 2
        else: #홀수
            ans += 1
            cur -= 1
    return ans

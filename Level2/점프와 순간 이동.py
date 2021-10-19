def solution(n):
    cur = n
    ans = 0
    while cur != 0:
        if cur % 2 == 0: #짝수
            cur /= 2
        else: #홀수
            ans += 1
            cur -= 1
    return ans

# 또는 이진수에서 1의 개수 세기

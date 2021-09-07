def solution(num):
    cnt = 0
    if num == 1:
        return cnt
    for _ in range(500):
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        cnt += 1
        if num == 1:
            return cnt
    return -1

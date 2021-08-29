def solution(n):
    return list(map(int, str(n)))[::-1]
    # 또는 return list(map(int, reversed(str(n))))

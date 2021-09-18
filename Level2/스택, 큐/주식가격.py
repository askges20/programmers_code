def solution(prices):
    n = len(prices)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            p = stack.pop()
            result[p] = i - p
        stack.append(i)
    while stack:
        p = stack.pop()
        result[p] = n - p - 1
    return result

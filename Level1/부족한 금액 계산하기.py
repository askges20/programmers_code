def solution(price, money, count):
    sum_cnt = count
    for i in range(1, count):
        sum_cnt += i
    diff = price * sum_cnt - money
    return diff if diff > 0 else 0

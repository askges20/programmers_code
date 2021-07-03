def solution(a, b):
    max_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    sum_days = b
    for i in range(1, a):
        sum_days += max_day[i-1]
    return days[sum_days%7]

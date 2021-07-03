def solution(a, b):
    max_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    return days[(sum(max_day[:a-1])+b)%7]

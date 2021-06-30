def solution(n):
    ternary = ""
    result = 0
    while True:
        ternary = str(n % 3) + ternary
        if n//3==0:
            break
        n = n//3
    for t in range(len(ternary)):
        result += int(ternary[t]) * pow(3,t)
    return result

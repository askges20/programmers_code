def solution(left, right):
    sum = 0
    for num in range(left, right + 1):
        cnt = 1
        for i in range(1,num//2 + 1):
            if num%i==0:
                cnt += 1
        if cnt%2==0:
            sum += num
        else:
            sum -= num
    return sum

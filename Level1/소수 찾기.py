import math

def isPrime(num):
    cnt = 0
    if num == 1:
        return False
    for k in range(1, num // 2 + 1):
        if num % k == 0:
            cnt += 1
        if cnt >= 2:
            return False
    return True
    
def solution(n): #에라토스테네스의 체
    nums = []
    cnt = 0
    for i in range(n + 1):
        nums.append('-')
    
    for j in range(1, int(math.sqrt(n))+1):
        if nums[j] == '-':
            if isPrime(j):
                nums[j] = 'o'
                for k in range(j, len(nums), j):
                    if nums[k] == '-':
                        nums[k] = 'x'
            else:
                nums[j] = 'x'
    for a in range(2, n + 1):
        if nums[a] != 'x':
            cnt += 1
    return cnt

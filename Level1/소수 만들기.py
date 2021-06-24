from itertools import combinations

def solution(nums):
    c = list(combinations(nums,3))
    cnt = 0
    for arr in c:
        tmp = 1
        for n in range(3,(sum(arr)//2)+1):
            if sum(arr)%n==0:
                tmp = 0
                break
        cnt += tmp
    return cnt
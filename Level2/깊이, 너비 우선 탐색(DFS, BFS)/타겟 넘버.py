def solution(numbers, target):
    return int(recursion(0, 0, "+", numbers, target) + recursion(0, 0, "-", numbers, target))

def recursion(sum, i, sign, numbers, target):
    if sign=="+":
        curSum = sum + numbers[i]
    else:
        curSum = sum - numbers[i]
        
    if i == len(numbers) - 1:
        if curSum == target:
            return 1
        else:
            return 0
    else:
        return recursion(curSum, i+1, "+", numbers, target) + recursion(curSum, i+1, "-", numbers, target)
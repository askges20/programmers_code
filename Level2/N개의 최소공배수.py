def solution(arr):
    answer = 1
    all_fac = {}
    for num in arr:
        fac = {}
        divisor = 2
        while num > 1:
            if num % divisor == 0:
                fac[divisor] = fac[divisor] + 1 if divisor in fac.keys() else 1
                num = int(num / divisor)
            else:
                divisor += 1
        for f in fac.keys():
            if f in all_fac.keys():
                if fac[f] <= all_fac[f]:
                    continue
            all_fac[f] = fac[f]
    for f in all_fac.keys():
        answer *= f**all_fac[f]
    return answer

def solution(s):
    cnt = 0
    del_zero = 0
    while s != '1':
        cnt += 1
        del_zero += s.count('0')
        s = bin(1 * s.count('1'))[2:]
    return [cnt, del_zero]

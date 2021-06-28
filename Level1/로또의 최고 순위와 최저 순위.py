def solution(lottos, win_nums):
    cnt_zero = lottos.count(0)
    cnt_match = 0
    for l in lottos:
        if l in win_nums:
            cnt_match += 1
    return [min(6, 7 - (cnt_match + cnt_zero)), min(6, 7 - cnt_match)]

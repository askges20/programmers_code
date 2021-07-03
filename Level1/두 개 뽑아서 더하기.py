from itertools import combinations

def solution(numbers):
    c_list = list(combinations(numbers,2))
    sum_set = set([])
    for c in c_list:
        sum_set.add(sum(c))
    sum_list = list(sum_set)
    sum_list.sort()
    return sum_list

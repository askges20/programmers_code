def solution(d, budget):
    d.sort()
    support=[]
    for e in d:
        if sum(support) + e > budget:
            break
        support.append(e)
    return len(support)

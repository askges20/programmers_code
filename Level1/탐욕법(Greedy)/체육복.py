#탐욕법(Greedy)
def solution(n, lost, reserve):
    L = set(lost) - set(reserve)
    R = set(reserve) - set(lost)
    print(type(L))
    
    for i in R:
        if i-1 in L:
            L.remove(i-1)
        elif i+1 in L:
            L.remove(i+1)
        
    return n-len(L)

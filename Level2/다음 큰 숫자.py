def solution(n):
    bin_n = bin(n)
    cur = n + 1
    while True:
        if bin_n.count("1") == bin(cur).count("1"):
            return cur
        cur += 1

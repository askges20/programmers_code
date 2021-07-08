def solution(n):
    bin_n_cnt = bin(n).count("1")
    cur = n + 1
    while True:
        if bin_n_cnt == bin(cur).count("1"):
            return cur
        cur += 1

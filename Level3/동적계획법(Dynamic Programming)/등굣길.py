def solution(n, m, puddles):
    loc = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    loc[1][1] = 1 #시작점
    for puddle in puddles:
        loc[puddle[0]][puddle[1]] = '0' #물에 잠긴 지역
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if loc[i][j] != '0': #물에 잠긴 지역이 아니면
                loc[i][j] = int(loc[i][j - 1]) + int(loc[i - 1][j])
    return loc[n][m] % 1000000007

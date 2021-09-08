def solution(dartResult):
    score = []
    num = ''
    for dr in dartResult:
        if dr.isnumeric():
            num += dr
        elif dr == 'S':
            score.append(int(num))
            num = ''
        elif dr == 'D':
            score.append(int(num)**2)
            num = ''
        elif dr == 'T':
            score.append(int(num)**3)
            num = ''
        elif dr == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
            score[-1] = score[-1] * 2
        elif dr == '#':
            score[-1] = score[-1] * -1
    return sum(score)

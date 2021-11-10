def solution(line):
    points, xlist, ylist = [], [], []
    for i in range(0, len(line) - 1):
        for j in range(i, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a * d - b * c: #평행하지 않을 때
                x = (b * f - d * e) / (a * d - b * c)
                y = (c * e - a * f) / (a * d - b * c)
                if x.is_integer() and y.is_integer():
                    points.append([int(x), int(y)])
                    xlist.append(int(x))
                    ylist.append(int(y))
    max_x, min_x = max(xlist), min(xlist)
    max_y, min_y = max(ylist), min(ylist)
    answer = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for x, y in points:
        answer[max_y - y][x - min_x] = '*'
    return [''.join(a) for a in answer]

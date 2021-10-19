def solution(dirs):
    cur_x, cur_y = 0, 0
    d = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
    visit = set()
    for i in range(len(dirs)):
        x, y = d[dirs[i]]
        new_x, new_y = cur_x + x, cur_y + y
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            visit.add((cur_x, cur_y, new_x, new_y))
            visit.add((new_x, new_y, cur_x, cur_y))
            cur_x, cur_y = new_x, new_y
    return len(visit)/2
